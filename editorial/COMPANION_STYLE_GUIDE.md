# Companion Style Guide — SEDA and MEDA

## 1. Purpose

This guide defines the writing style for the SEDA and MEDA companions.

The desired voice is practical, direct, pedagogical, and statistically careful.

The reader should feel guided by someone who understands both the method and the real interface, not by a software manual and not by an academic article.

## 2. Reference voice

The companion voice can be summarized as:

> A scientist sitting beside the reader, explaining what to do, why it matters, what the software is calculating, and how to read the result without overclaiming.

The tone should remain simple without becoming simplistic.

## 3. Start with the analytical question

Open a method with the question it answers.

Prefer:

> This analysis answers two complementary questions: which attributes differentiate the products, and which attributes characterize each product?

Avoid beginning with:

> Open SEDA and select Characterization of the Stimulus Space.

The interface follows the question.

## 4. Be pragmatic

Every paragraph should help the reader do at least one of the following:

```text
choose the analysis
prepare the data
understand the mechanism
set an option
read an output
avoid a mistake
interpret the evidence
reproduce the workflow
```

If a paragraph does none of these things, shorten or remove it.

## 5. Explain only what changes understanding or action

Technical detail is justified when it affects:

```text
what the analysis calculates
what the user should select
what the result represents
how the result should be interpreted
```

Do not add a statistical derivation merely because it is rigorous.

Do not add a software detail merely because it exists.

## 6. Use the same language for the interface and the text

When referring to an actual jamovi field, option, table, or graph, reproduce its current interface label exactly.

For example:

```text
Stimulus Effect
Subject Effect
Sensory Attributes
Scale to unit variance
```

Then explain the statistical role in ordinary language.

This makes it possible for the reader to move directly between the text and the interface.

## 7. Describe interface fields through statistical roles

For an important variable field, prefer the pattern:

```text
Role
What the variable represents in the analysis.

Impact on the analysis
What changes statistically when this field is populated.

Check before running
One practical validation point when useful.
```

Avoid repeating obvious instructions such as “drag the variable into the field” when the field name and procedure already make this clear.

## 8. Describe options through consequences

For an important option, answer three questions:

```text
What is it?
What does it change statistically?
When should I change it?
```

When useful, classify it explicitly as:

```text
Display option
```

or:

```text
Analytical option
```

Do not imply that an option is important merely because it appears in the interface.

## 9. Keep the step-by-step procedure short

The procedure is a checklist, not a second explanation of the chapter.

It should tell the reader how to reproduce the workflow efficiently.

Detailed statistical explanations belong in *Understanding what happens under the hood* or *Interpretation of results*.

## 10. Under the hood should remain readable

The purpose of *Understanding what happens under the hood* is to remove the black box.

It should explain concepts such as:

```text
reference
product or subject effect
adjusted mean
contingency table
factorial space
active / supplementary information
resampling
penalty
clustering
```

only as far as needed for correct interpretation.

Prefer conceptual statements to formulas unless a formula genuinely clarifies the mechanism.

## 11. Statistical evidence comes first

When interpreting an output, use this order:

```text
1. What does the output contain?
2. Which evidence matters here?
3. What does that evidence mean?
4. What conclusion is justified?
5. What common overinterpretation should be avoided?
```

Do not move directly from a visual impression to a substantive conclusion.

## 12. Translate statistical evidence into scientific meaning

When useful, explicitly move from statistical language to sensory or multivariate meaning.

For example:

```text
The Product effect is significant.
→ The products were differentiated on this attribute.
```

or:

```text
The first two PCA dimensions explain 65% of the inertia.
→ The displayed plane summarizes a substantial, but not complete, part of the multivariate structure.
```

The second sentence should add meaning, not merely rephrase the first.

## 13. Do not narrate visible outputs

Avoid describing everything the reader can already see.

Weak:

> Product A is on the right, Product B is on the left, and Product C is near the centre.

Better:

> The main contrast separates Product A from Product B; the attribute representation shows which variables define this opposition, while Product C remains comparatively close to the average profile on this plane.

Text should identify evidence and explain why it matters.

## 14. Keep examples synthetic but complete

A worked example should not become a transcript of every output.

Prefer:

```text
settings
→ first evidence to inspect
→ second evidence if needed
→ combined interpretation
→ limit or caution
```

A *Synthetic interpretation* should integrate several outputs into one coherent conclusion.

## 15. Practical tips must be practical

A practical tip should solve a real local problem.

Good topics include:

```text
incorrect variable type
sparse results
wrong reference level
insufficient number of variables or terms
poor representation on the selected plane
interpretation of an absent table or graph
choice between display and analytical options
```

Avoid generic advice such as “interpret carefully” unless the text specifies what to check.

## 16. Use warnings sparingly

A warning is justified when a plausible action could lead to a wrong analysis or a wrong conclusion.

Do not turn every nuance into a warning box.

Too many warnings make genuine warnings invisible.

## 17. Avoid filler

Treat the following as warning signs when they do not add precise meaning:

```text
important
powerful
valuable insights
very useful
remarkably
highly
robust
comprehensive
key feature
```

Explain the consequence instead.

## 18. Keep sentences functional

For any sentence, ask:

> If this sentence disappeared, what would the reader lose?

Acceptable answers include:

```text
an instruction
an explanation
a statistical meaning
a practical warning
a limitation
a connection between interface and method
an interpretation
```

If nothing precise would be lost, shorten, merge, or remove the sentence.

## 19. One paragraph, one dominant job

A paragraph should normally do one main thing:

```text
motivate
explain
instruct
interpret
warn
transition
```

Do not mix interface instructions, statistical theory, interpretation, and practical advice in one dense paragraph.

## 20. Preserve chapter autonomy without duplication

A reader may enter the companion directly through one method.

Each chapter must therefore provide enough context to stand on its own.

However, autonomy does not require repeating full explanations already available elsewhere.

Use concise reminders and cross-references when a general concept has already been explained thoroughly.

This will be especially important between SEDA and MEDA.

## 21. SEDA and MEDA should sound related, not identical

### SEDA vocabulary

Prefer the language of the sensory task:

```text
stimulus / product
subject / consumer
sensory attribute
term
defect
liking
individual map
categorization
```

### MEDA vocabulary

Prefer the language of the multivariate object:

```text
individual
variable
modality
row / column profile
group of variables
active element
supplementary element
factorial dimension
cluster
```

Do not force one vocabulary onto the other when the statistical object differs.

## 22. Use “product” and “stimulus” consistently

When a specific interface uses *Stimulus*, preserve the interface label exactly.

In explanatory prose, use the terminology most natural for the example, but avoid unnecessary switching within the same passage.

If the companion defines product and stimulus as equivalent terms, maintain that convention consistently.

## 23. R code should expose, not distract

When a *From jamovi to R* section is included:

```text
identify the statistical implementation
connect major jamovi options to major R arguments
show only the code needed to make the connection clear
```

Do not teach generic R syntax there.

Do not document an exact function signature until it has been validated against the current module.

## 24. Prefer reproducible references

When writing in Quarto, use identifiers for figures, tables, sections, citations, and chapters whenever possible.

Avoid hard-coded numbering that may break when the companion changes.

## 25. Final style principle

> Clear enough to use immediately; rigorous enough not to mislead; short enough to remain a companion.
