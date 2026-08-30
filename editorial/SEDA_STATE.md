# SEDA State — Companion

## 1. Purpose

This file is the operational dashboard for revising the SEDA companion.

It does not replace the editorial rules in:

```text
COMPANION_CHARTER.md
COMPANION_STYLE_GUIDE.md
COMPANION_CHAPTER_TEMPLATE.md
COMPANION_METHOD_MAPPING.md
```

Its role is simpler:

```text
know what has been validated
know what still has to be checked
know which source files are authoritative
know which chapter is currently being revised
know when a chapter is ready to commit
```

Update this file whenever the status of an analysis changes materially.

---

## 2. Current project baseline

### Repository

```text
Repository: Sebastien-Le/seda-book
Branch: main
Bilingual Quarto profiles: installed and validated
French profile: fr
English profile: en
```

Validated build commands:

```bash
quarto render --profile fr
quarto render --profile en
```

Both profiles have been validated for HTML and PDF rendering.

### Editorial baseline

```text
French source family: *_prompt_harmonise.qmd
English source family: *_prompt_GBH.qmd
French introduction: intro_ppt.qmd
English introduction: intro_ppt_GB.qmd
French preface: _preface-fr.qmd
English preface: _preface-en.qmd
Shared entry point: index.qmd
```

### Software baseline

```text
SEDA repository: Sebastien-Le/SEDA
SEDA master version: 1.4.2
jamovi version used for companion validation: TO CONFIRM
```

SEDA `master` currently declares version **1.4.2** in `DESCRIPTION`.

The exact interface baseline must still be confirmed by running the current module in jamovi.

Do not infer current interface behavior from the previous companion alone.

Software truth follows:

```text
validated current module behavior
>
current module implementation / generated R code when relevant
>
companion text
```

---

## 3. Status vocabulary

```text
NOT STARTED
SOFTWARE VERIFIED
SCIENCE VERIFIED
REVISED FR
REVISED EN
RENDERED
VALIDATED
COMPLETE
```

- **NOT STARTED** — existing chapter identified, but no current audit performed.
- **SOFTWARE VERIFIED** — current menu, fields, options, defaults, outputs, and R Code behavior checked in jamovi.
- **SCIENCE VERIFIED** — statistical mechanism and interpretation checked against the actual implementation.
- **REVISED FR** — French source updated.
- **REVISED EN** — English source updated consistently with the validated version.
- **RENDERED** — both language profiles render successfully after revision.
- **VALIDATED** — worked example and interpretation checked against current outputs.
- **COMPLETE** — chapter committed and pushed with no known blocking issue.

---

## 4. Analysis tracker

| # | Analysis | French source | English source | Main cross-method link | Status | Main outstanding work |
|---|---|---|---|---|---|---|
| 1 | QDA — Characterization of the stimulus space | `chapitre1_prompt_harmonise.qmd` | `chapitre1_prompt_GBH.qmd` | adjusted means / product and subject effects | NOT STARTED | Full software + scientific audit |
| 2 | QDA — Multivariate representation with ellipses | `chapitre2_prompt_harmonise.qmd` | `chapitre2_prompt_GBH.qmd` | PCA / resampling / confidence regions | NOT STARTED | Full software + scientific audit |
| 3 | CATA | `chapitre3_prompt_harmonise.qmd` | `chapitre3_prompt_GBH.qmd` | CA / characterization / clustering | NOT STARTED | Full software + scientific audit |
| 4 | JAR | `chapitre4_prompt_harmonise.qmd` | `chapitre4_prompt_GBH.qmd` | defects / CA / penalty analysis | NOT STARTED | Full software + scientific audit |
| 5 | Napping | `chapitre5_prompt_harmonise.qmd` | `chapitre5_prompt_GBH.qmd` | MFA / grouped coordinates | NOT STARTED | Full software + scientific audit |
| 6 | Sorting | `chapitre6_prompt_harmonise.qmd` | `chapitre6_prompt_GBH.qmd` | MCA / categorizations / textual information | NOT STARTED | Full software + scientific audit |
| 7 | Preference Mapping | `chapitre7_prompt_harmonise.qmd` | `chapitre7_prompt_GBH.qmd` | upstream MEDA PCA + preference modelling | NOT STARTED | Full software + scientific audit |

---

## 5. Global items to validate once

### Module identity

```text
SEDA version:
jamovi version:
module menu label:
analysis menu paths:
R Code availability:
Read me / integrated help behavior:
```

### Common interface conventions

```text
terminology: stimulus / product
terminology: subject / consumer
variable-type requirements
missing-value behavior where shared
common plot export behavior
common R Code labeling and availability
common output naming conventions
```

### Reproducibility convention

For every chapter where R Code is discussed:

```text
jamovi option
↔
statistical consequence
↔
generated R code / underlying R call
```

Do not document an exact R signature until it has been checked against the current module.

---

## 6. Per-analysis audit record

Use this compact record for each analysis.

### Analysis name

```text
Status:
French source:
English source:
Menu path:
Validated dataset:
SEDA version:
jamovi version:
Underlying R package(s):
Cross-reference to MEDA, if useful:
```

#### A. Analytical question

```text
What question does the analysis answer?
What data structure does it require?
What is the main statistical object?
```

#### B. Software truth

Verify:

```text
menu path
analysis title
variable fields
field labels
option labels
default values
analytical versus display options
conditional options
output table names
output graph names
conditions controlling outputs
R Code availability
```

#### C. Statistical mechanism

Verify:

```text
what enters the calculation
what is estimated / tested / represented
reference or comparison
selection / weighting / resampling logic
uncertainty where applicable
clustering logic where applicable
```

#### D. Evidence and interpretation

Record:

```text
first output to inspect
main evidence
secondary evidence
correct substantive interpretation
main overinterpretation to avoid
```

#### E. Worked example

Verify:

```text
dataset available in current SEDA distribution
variable assignments
options
numerical outputs
figures
synthetic interpretation
```

#### F. R bridge

Record only if useful:

```text
underlying package / method
major jamovi-to-R correspondences
what generated R Code reproduces
what should remain outside the companion
```

#### G. Editorial actions

Classify revisions as:

```text
SCIENTIFIC CORRECTION
PEDAGOGICAL CLARIFICATION
SOFTWARE UPDATE
INTERFACE UPDATE
EXAMPLE UPDATE
EDITORIAL SIMPLIFICATION
```

#### H. Validation

```text
French render: pending / pass
English render: pending / pass
Example reproduced: pending / pass
R Code checked: not applicable / pending / pass
Git commit:
Outstanding issue:
```

---

## 7. Cross-companion boundaries

```text
SEDA QDA ellipses
→ sensory-specific profile construction and resampling in SEDA
→ general PCA reading in MEDA

SEDA CATA
→ CATA-specific aggregation and characterization in SEDA
→ general CA geometry in MEDA

SEDA Napping
→ Napping data structure and interpretation in SEDA
→ general MFA logic in MEDA

SEDA Sorting
→ free-sorting structure in SEDA
→ general MCA logic in MEDA

SEDA Preference Mapping
→ preference modelling in SEDA
→ upstream PCA space in MEDA
```

Cross-references should reduce duplication without making the SEDA chapter unusable on its own.

---

## 8. Revision order

```text
1. QDA — Characterization
2. QDA — Ellipses
3. CATA
4. JAR
5. Napping
6. Sorting
7. Preference Mapping
```

Preserve this order unless the audit reveals a strong pedagogical reason to change it.

---

## 9. Chapter workflow

```text
1. Validate current SEDA behavior in jamovi.
2. Record the software truth in this file.
3. Validate the statistical mechanism.
4. Compare with the current French and English sources.
5. Revise only what improves correctness, understanding, reproducibility, or practical use.
6. Validate the worked example.
7. Check R Code when relevant.
8. Render FR and EN.
9. Inspect the rendered chapter.
10. Update this state file.
11. Review Git diff.
12. Commit and push.
```

Recommended Git checkpoint:

```bash
git status -sb
git diff --check
git diff
git add <targeted files>
git diff --cached --check
git diff --cached
git commit -m "..."
git push origin main
```

---

## 10. Current next action

### Chapter 1 — QDA Characterization of the stimulus space

Start with a software-first audit.

Before editing either language source, record:

```text
current SEDA version
current jamovi version
exact menu path
exact field labels
all options and defaults
all current outputs
conditions under which outputs appear
R Code behavior
validated example dataset
```

Then compare current module behavior with:

```text
chapitre1_prompt_harmonise.qmd
chapitre1_prompt_GBH.qmd
```

No prose revision should begin until this baseline is established.

---

## 11. Final rule

> The state file records decisions and validation status. The companion chapters teach the method. The module defines the current software truth.
