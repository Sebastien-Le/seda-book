#!/usr/bin/env python3
"""
Apply companion illustrations described in editorial/ILLUSTRATIONS.json.

Design goals:
- no manual editing of .qmd files;
- exact anchors only;
- idempotent: a figure already present is not duplicated;
- fail closed: ambiguous/missing anchors stop the script;
- touch only the requested chapter source files.
"""

from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "editorial" / "ILLUSTRATIONS.json"


def die(msg: str) -> None:
    raise SystemExit(f"ERROR: {msg}")


def load_manifest() -> dict:
    if not MANIFEST.exists():
        die(f"manifest not found: {MANIFEST}")
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def figure_block(fig: dict) -> str:
    ref = fig.get("reference", "").strip()
    ref_pos = fig.get("reference_position", "after")
    img = (
        f'![{fig["caption"]}]({fig["image"]})'
        f'{{#{fig["id"]} width={fig["width"]} fig-align="center"}}'
    )

    if not ref:
        return img
    if ref_pos == "before":
        return f"{ref}\n\n{img}"
    if ref_pos == "after":
        return f"{img}\n\n{ref}"
    die(f'unknown reference_position for {fig["id"]}: {ref_pos}')


def validate_existing(text: str, fig: dict, source: Path) -> None:
    fig_id = fig["id"]
    if f"#{fig_id}" not in text:
        die(f"{source}: expected figure id #{fig_id} not found")
    if f"@{fig_id}" not in text:
        die(f"{source}: expected cross-reference @{fig_id} not found")
    image = ROOT / fig["image"]
    if not image.exists():
        die(f"image not found: {image}")


def insert_figure(text: str, fig: dict, source: Path) -> tuple[str, str]:
    fig_id = fig["id"]
    image = ROOT / fig["image"]
    if not image.exists():
        die(f"image not found: {image}")

    if f"#{fig_id}" in text:
        if f"@{fig_id}" not in text:
            die(f"{source}: #{fig_id} exists but @{fig_id} is missing")
        return text, "already present"

    if fig.get("validation_only", False):
        die(
            f"{source}: {fig_id} is marked validation_only and is missing. "
            "Do not reconstruct this pilot figure automatically."
        )

    anchor = fig["anchor_line"]
    occurrences = text.count(anchor)
    if occurrences != 1:
        die(
            f"{source}: anchor for {fig_id!r} must occur exactly once; "
            f"found {occurrences}: {anchor}"
        )

    block = figure_block(fig)
    position = fig.get("position", "after")

    if position == "before":
        replacement = f"{block}\n\n{anchor}"
    elif position == "after":
        replacement = f"{anchor}\n\n{block}"
    else:
        die(f"{source}: unknown position for {fig_id}: {position}")

    return text.replace(anchor, replacement, 1), "inserted"


def process_language(lang: str, cfg: dict, dry_run: bool) -> list[str]:
    source = ROOT / cfg["source"]
    if not source.exists():
        die(f"source not found: {source}")

    original = source.read_text(encoding="utf-8")
    text = original
    messages = []

    for fig in cfg.get("figures", []):
        text, action = insert_figure(text, fig, source)
        messages.append(f"{lang}: {fig['id']}: {action}")

    if text != original and not dry_run:
        source.write_text(text, encoding="utf-8")

    # Always validate the resulting text.
    for fig in cfg.get("figures", []):
        validate_existing(text, fig, source)

    return messages


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--chapter",
        required=True,
        help="chapter key from editorial/ILLUSTRATIONS.json, e.g. qda-multi or cata",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate and show intended actions without writing files",
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
    print(f"Chapter: {args.chapter} — {chapter.get('label', '')}")

    all_messages = []
    for lang in ("fr", "en"):
        cfg = chapter.get("languages", {}).get(lang)
        if cfg is None:
            die(f"{args.chapter}: missing language configuration: {lang}")
        all_messages.extend(process_language(lang, cfg, args.dry_run))

    for msg in all_messages:
        print("  " + msg)

    print("OK — sources and figure references validated.")
    if args.dry_run:
        print("Dry run: no file was written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
