#!/usr/bin/env python3
"""
Render, validate, and optionally publish companion illustrations.

Examples:
  python scripts/publish_companion.py --chapter qda-multi --check
  python scripts/publish_companion.py --chapter qda-multi --publish

The script never commits or pushes.
"""

from __future__ import annotations
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "editorial" / "ILLUSTRATIONS.json"


def die(msg: str) -> None:
    raise SystemExit(f"ERROR: {msg}")


def run(cmd: list[str], *, capture: bool = False) -> str:
    print("+", " ".join(cmd))
    proc = subprocess.run(
        cmd,
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=capture,
    )
    if proc.returncode != 0:
        if capture:
            sys.stderr.write(proc.stdout or "")
            sys.stderr.write(proc.stderr or "")
        die(f"command failed ({proc.returncode}): {' '.join(cmd)}")
    return proc.stdout if capture else ""


def load_manifest() -> dict:
    if not MANIFEST.exists():
        die(f"manifest not found: {MANIFEST}")
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def git_branch() -> str:
    return run(["git", "branch", "--show-current"], capture=True).strip()


def validate_sources(chapter: dict) -> None:
    for lang, cfg in chapter["languages"].items():
        source = ROOT / cfg["source"]
        if not source.exists():
            die(f"source not found: {source}")
        text = source.read_text(encoding="utf-8")
        for fig in cfg.get("figures", []):
            if f"#{fig['id']}" not in text:
                die(f"{source}: missing #{fig['id']}")
            if f"@{fig['id']}" not in text:
                die(f"{source}: missing @{fig['id']}")
            image = ROOT / fig["image"]
            if not image.exists():
                die(f"image not found: {image}")


def render() -> None:
    run(["quarto", "render", "--profile", "fr"])
    run(["quarto", "render", "--profile", "en"])


def validate_rendered(manifest: dict, chapter: dict) -> None:
    profiles = manifest["profiles"]
    for lang, cfg in chapter["languages"].items():
        render_dir = ROOT / profiles[lang]["render_dir"]
        html = render_dir / cfg["rendered_html"]
        if not html.exists():
            die(f"rendered HTML not found: {html}")
        text = html.read_text(encoding="utf-8", errors="replace")
        for fig in cfg.get("figures", []):
            if fig["id"] not in text:
                die(f"{html}: rendered figure id missing: {fig['id']}")
            if Path(fig["image"]).name not in text:
                die(f"{html}: rendered image filename missing: {fig['image']}")
            rendered_image = render_dir / fig["image"]
            if not rendered_image.exists():
                die(f"rendered image not found: {rendered_image}")
        print(f"OK rendered {lang}: {html.relative_to(ROOT)}")


def copy_file(src: Path, dst: Path) -> None:
    if not src.exists():
        die(f"publish source not found: {src}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"COPY {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")


def publish(manifest: dict, chapter: dict) -> None:
    profiles = manifest["profiles"]

    for lang, cfg in chapter["languages"].items():
        profile = profiles[lang]
        render_dir = ROOT / profile["render_dir"]
        publish_dir = ROOT / profile["publish_dir"]

        copy_file(
            render_dir / cfg["rendered_html"],
            publish_dir / cfg["rendered_html"],
        )

        # Copy only the figures used by this chapter.
        for fig in cfg.get("figures", []):
            copy_file(
                render_dir / fig["image"],
                publish_dir / fig["image"],
            )

        # Search index and full PDF depend on the rendered book, so refresh both.
        copy_file(
            render_dir / profile["search_file"],
            publish_dir / profile["search_file"],
        )
        copy_file(
            render_dir / profile["pdf"],
            publish_dir / profile["pdf"],
        )


def show_git_checks() -> None:
    run(["git", "diff", "--check"])
    print("\n--- git status --short ---")
    print(run(["git", "status", "--short"], capture=True), end="")
    print("\n--- docs diff --stat ---")
    print(run(["git", "diff", "--stat", "--", "docs"], capture=True), end="")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapter", required=True)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--publish", action="store_true")
    parser.add_argument(
        "--no-render",
        action="store_true",
        help="reuse current _render output instead of rendering again",
    )
    args = parser.parse_args()

    manifest = load_manifest()
    chapters = manifest.get("chapters", {})
    if args.chapter not in chapters:
        die(
            f"unknown chapter {args.chapter!r}. Available: "
            + ", ".join(sorted(chapters))
        )
    chapter = chapters[args.chapter]

    print(f"Branch: {git_branch()}")
    validate_sources(chapter)

    if not args.no_render:
        render()

    validate_rendered(manifest, chapter)

    if args.publish:
        publish(manifest, chapter)

    show_git_checks()

    if args.check:
        print("\nOK — render and validation completed; docs were not modified.")
    else:
        print(
            "\nOK — publication files copied to docs/. "
            "Review the diff, then stage/commit/push manually."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
