# Companion illustration workflow

Prototype based on the stabilised QDA multivariate chapter.

Files:
- `editorial/ILLUSTRATIONS.json`: declarative figure manifest.
- `images/<chapter>/`: human-approved final illustration files. Prepare and approve these images outside Codex, then place them directly in this directory. Automation must not crop, resize, redraw, or otherwise modify their pixels; it may only control their display size through Quarto figure attributes.
- `illustrations/inbox/`: optional ignored area for raw screenshots. Raw screenshots are never committed and are not required for the normal workflow.
- `scripts/apply_illustrations.py`: inserts/validates figures in FR and EN `.qmd`.
- `scripts/publish_companion.py`: renders, validates and copies only the chapter outputs, figures, search indexes and PDFs into `docs/`.

The scripts never commit or push.

Initial smoke test on the existing pilot:

```bash
python scripts/apply_illustrations.py --chapter qda-multi --dry-run
python scripts/publish_companion.py --chapter qda-multi --check
```

For a future chapter, add its FR/EN files, figure metadata and insertion anchors to `editorial/ILLUSTRATIONS.json`, then run the same two commands with the new chapter key.
