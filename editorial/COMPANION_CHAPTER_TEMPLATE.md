# Companion Chapter Template — SEDA and MEDA

## 1. Purpose

This template defines the standard workflow for creating or revising one analysis chapter in the SEDA or MEDA companion.

It is intentionally lighter than the book revision workflow.

The chapter is both:

```text
a practical jamovi guide
and
a compact methodological guide
```

The default workflow is:

```text
validate the current module
↓
review the current chapter or define the new one
↓
check statistical mechanism
↓
check interface
↓
check outputs
↓
validate worked example
↓
revise text
↓
render and inspect
↓
Git checkpoint
```

## 2. Chapter identity

Record:

```text
Companion: SEDA / MEDA

Analysis name:

Menu path:

Main analytical question:

Expected data structure:

Main statistical method(s):

Underlying R package(s):

Validated example dataset:

Related chapter in the other companion, if any:

Related chapter in Analyzing Sensory Data with R, if useful:
```

Exact implementation details should be recorded only after validation against the current module.

## 3. Validate software truth first

Before editing the prose, run the current validated module and record the real interface.

Check:

```text
menu path
analysis title
variable fields
option labels
default values
collapsed / expanded sections
conditions controlling outputs
result table names
result graph names
data outputs
R Code availability and content
integrated help / Read me behavior
```

Do not revise from the old companion alone.

If the old companion and current module disagree, the current validated module is the reference.

## 4. Validate the statistical mechanism

Write a short answer to each question:

```text
What analytical question does the method answer?

What data actually enter the calculation?

What statistical object is constructed?

What is being estimated, tested, represented, or grouped?

What is the relevant reference or comparison?

Which analytical choices can change the result?

What evidence is produced?

What is the most likely misinterpretation?
```

This forms the basis of *Understanding what happens under the hood* and *Interpretation of results*.

## 5. Default chapter structure

Use the following structure unless the method requires a justified variation.

```text
# Analysis title

## Introduction
## Understanding what happens under the hood
## Expected data structure
## Interface guide
## Step-by-step procedure
## Interpretation of results
## Example: ...
## From jamovi to R          [optional]
## Practical tips
## In summary
```

The order may be adjusted when necessary, but the reader should always understand the progression from question to result.

## 6. Introduction

### Purpose

Answer quickly:

```text
What kind of data is this analysis for?

What question does it answer?

What does it add compared with a simpler alternative?
```

Where useful, identify the example dataset that will be used later.

### Keep it short

The introduction should orient the reader, not teach the entire method.

## 7. Understanding what happens under the hood

### Purpose

Explain enough of the statistical mechanism to prevent black-box use.

Possible subsections include:

```text
data checking and transformation
model or reference structure
selection step
construction of a factorial space
active and supplementary information
resampling
classification
penalty calculation
preference modelling
```

### Required test

For every subsection, ask:

> Will this explanation change how the reader sets the analysis or interprets a result?

If not, shorten or remove it.

## 8. Expected data structure

State concretely:

```text
what one row represents
what the key columns represent
required variable types
required ordering or grouping constraints
whether missing values are acceptable or consequential
whether supplementary variables are possible
```

When useful, include a compact schematic table.

The reader should be able to compare this description with their own dataset before opening the analysis.

## 9. Interface guide

### 9.1 Variable fields

For each important field, use:

```text
### [Current interface label]

Role:

Impact on the analysis:

Check before running: [only when useful]
```

### 9.2 Options

For each important option, use:

```text
### [Current interface label]

Type: Display option / Analytical option

What it controls:

Statistical consequence:

When to change it:
```

Shorten the pattern when one of these items is self-evident.

### 9.3 Conditional options

If an option is available only under certain conditions, state those conditions explicitly.

Avoid vague formulations such as “if available”.

## 10. Step-by-step procedure

The procedure should be reproducible and compact.

A useful pattern is:

```text
1. Open the dataset.
2. Check variable types.
3. Open the analysis.
4. Assign the variables.
5. Keep or change the main analytical options.
6. Read output A first.
7. Read output B next.
8. Request optional output C only if needed.
```

Do not repeat explanations already given in the interface guide.

## 11. Interpretation of results

For each major output, answer:

```text
What does this output represent?

Which columns, numbers, or geometric relationships matter?

What is the correct reading order?

How does this translate into substantive meaning?

What should not be concluded from it?
```

When a table contains several columns, a compact *Element / Meaning* table may be used.

When a graph is involved, explain the geometry before interpreting the example.

## 12. Worked example

### 12.1 Dataset

Use a dataset that is available, stable, and validated for the current module.

Explain only the context needed to understand the analysis.

### 12.2 Example settings

Provide a compact table of the exact settings required to reproduce the example.

### 12.3 Reading strategy

Do not discuss outputs in software order automatically.

Discuss them in analytical order.

For example:

```text
global evidence
↓
local evidence
↓
multivariate representation
↓
uncertainty or classification
↓
synthetic interpretation
```

### 12.4 Synthetic interpretation

End the example with a short integrated interpretation.

It should combine the main evidence rather than summarize each output separately.

State an important limitation when one is relevant.

## 13. From jamovi to R — optional

Include this section when the module exposes useful reproducible R code or when the R connection materially improves understanding.

Cover only:

```text
underlying R package / method
main correspondence between jamovi fields or options and the R analysis
what the generated code reproduces
how the reader could extend the analysis in R
```

Do not duplicate the R book.

Do not include unstable implementation detail without a validated baseline.

## 14. Practical tips

Keep this section short.

Prioritize real failure modes and recurring decisions:

```text
wrong variable type
wrong reference
sparse results
insufficient variables / terms
poor factorial representation
unexpected absent outputs
large number of categories
choice of threshold
interpretation of uncertainty
choice of clustering output
```

Each tip should lead to an action or a check.

## 15. In summary

Use a short recap organized around the analytical workflow rather than around the menu.

A useful structure is:

```text
Use this analysis when...

The analysis works by...

Read ... first, then ...

Remember that...
```

Avoid repeating the chapter introduction word for word.

## 16. SEDA-specific checks

For SEDA analyses, verify when relevant:

```text
stimulus / product role
subject / consumer role
sensory attribute role
liking role
term / defect coding
repeated evaluations
adjusted means
sensory-specific references
panel variability
consumer interpretation
```

Keep the sensory question visible throughout the chapter.

## 17. MEDA-specific checks

For MEDA analyses, verify when relevant:

```text
what the statistical individuals are
what the active variables are
whether standardization is applied
what is supplementary
what distance / profile geometry is being analyzed
what the axes optimize or summarize
how much inertia is represented
coordinates versus contributions versus cos²
which dimensions feed clustering
how clusters are characterized
```

The interface should help the reader understand the multivariate object, not merely produce a map.

## 18. Cross-companion reuse

Before repeating a substantial explanation, check whether the other companion should be the primary reference.

Examples:

```text
PCA foundations
    primary detailed treatment: MEDA
    SEDA: explain only what the sensory workflow requires

MFA foundations
    primary detailed treatment: MEDA
    SEDA Napping: explain the specific unstandardized grouped-coordinate logic

MCA foundations
    primary detailed treatment: MEDA
    SEDA Sorting: explain the specific individual-categorization logic
```

A cross-reference should reduce duplication without making the current chapter unusable on its own.

## 19. Chapter validation checklist

### Statistical

- [ ] The analytical question is clear.
- [ ] The described statistical mechanism matches the current implementation.
- [ ] References, comparisons, and uncertainty are correctly described.
- [ ] Statistical evidence and interpretation are separated.
- [ ] Limitations are stated where they change the reading.

### Interface

- [ ] Menu path is current.
- [ ] Field names are current.
- [ ] Option names and defaults are current.
- [ ] Analytical and display options are not confused.
- [ ] Conditional outputs are documented correctly.

### Example

- [ ] Dataset is available.
- [ ] Settings reproduce the intended analysis.
- [ ] Numerical and graphical outputs match the text.
- [ ] Synthetic interpretation is supported by the results.

### R bridge

- [ ] Generated R Code has been checked when discussed.
- [ ] R function/package statements are current.
- [ ] The text does not imply more reproducibility than the module actually provides.

### Editorial

- [ ] The chapter is pragmatic and readable.
- [ ] Step-by-step instructions are not duplicated in prose.
- [ ] Outputs are interpreted rather than merely described.
- [ ] Cross-references reduce duplication.
- [ ] jamovi is written in lowercase.

### Render

- [ ] Quarto render succeeds.
- [ ] Tables and figures are legible.
- [ ] Callouts do not overwhelm the page.
- [ ] Cross-references resolve.
- [ ] Several consecutive pages have a readable rhythm.

## 20. Revision log

At completion, record briefly:

```text
Analysis:

Status: audited / revised / rendered / validated / committed

Scientific corrections:

Interface updates:

Pedagogical clarifications:

Example changes:

R bridge: none / added / revised

Outstanding issues:
```

## 21. Git checkpoint

After validation:

```text
git status
git diff --check
git diff
targeted git add
git diff --cached --check
git diff --cached
precise commit
git status
```

The commit message should describe the purpose of the revision, for example:

```text
Update SEDA CATA companion for current interface

Clarify PCA interpretation in MEDA companion

Align JAR penalty documentation with current output
```

## 22. Final principle

> Validate the software, explain the method, guide the action, interpret the evidence.
