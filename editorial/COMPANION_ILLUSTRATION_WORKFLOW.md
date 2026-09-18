# Companion illustration workflow

Prototype based on the stabilised QDA multivariate chapter.

Files:
- `editorial/ILLUSTRATIONS.json`: declarative figure manifest.
- `scripts/apply_illustrations.py`: inserts/validates figures in FR and EN `.qmd`.
- `scripts/publish_companion.py`: renders, validates and copies only the chapter outputs, figures, search indexes and PDFs into `docs/`.

The scripts never commit or push.

Initial smoke test on the existing pilot:

```bash
python scripts/apply_illustrations.py --chapter qda-multi --dry-run
python scripts/publish_companion.py --chapter qda-multi --check
```

For a future chapter, add its FR/EN files, figure metadata and insertion anchors to `editorial/ILLUSTRATIONS.json`, then run the same two commands with the new chapter key.
