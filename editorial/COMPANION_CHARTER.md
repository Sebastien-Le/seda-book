# Companion Charter — SEDA and MEDA

## 1. Purpose

The SEDA and MEDA companions are practical guides for using statistical methods in jamovi **with understanding**.

Their purpose is not to reproduce a statistics textbook, nor to document every software detail. They should help a reader move from a real analytical question to a correctly interpreted result while progressively becoming less dependent on the interface.

The common path is:

```text
question
↓
data structure
↓
statistical method
↓
jamovi interface
↓
statistical evidence
↓
interpretation
↓
reproducible R path when useful
```

The companions should be pragmatic, pedagogical, and concise.

## 2. The central promise: progressive autonomy

A companion should help the reader move from:

```text
Show me where to click.
```

toward:

```text
I know why I am doing this,
what the main options change,
what the output represents,
and how to interpret it.
```

The objective is not immediate expertise. It is reliable autonomy.

A useful chapter gives the reader enough statistical understanding to avoid common misinterpretations and enough software guidance to reproduce the analysis on their own data.

## 3. Pragmatic pedagogy

The companion should explain **only the technical detail that changes how the analysis is run or interpreted**.

Include an explanation when it answers a practical question such as:

```text
What is being compared?
Compared with what?
What constructs the map?
What is supplementary?
What does this threshold change?
What does this ellipse represent?
What does this penalty represent?
What does this cluster depend on?
What does this option change statistically?
```

Do not add mathematical or software detail simply because it is available.

The working rule is:

> Enough statistics to understand. Enough interface guidance to act. Enough interpretation to decide. No more than necessary.

## 4. Method before interface

The interface is central to a companion, but it should never become the conceptual starting point.

Prefer:

```text
We want to identify which attributes differentiate the products.
The analysis therefore tests the product effect attribute by attribute.
In SEDA, the product identifier is placed in Stimulus Effect.
```

rather than:

```text
Drag Product into Stimulus Effect.
```

Every important interface field should be connected to a statistical role.

Every important option should be connected to its analytical consequence.

Every important output should be connected to the evidence it contains.

## 5. Interfaces without black boxes

jamovi makes analyses accessible. Accessibility must not hide the statistical mechanism.

The preferred progression is:

```text
understand
→ click
→ inspect
→ interpret
→ reconnect to R when useful
```

The companion should distinguish between:

```text
interface action
and
statistical meaning
```

and between:

```text
display option
and
analytical option
```

A display option changes how an existing result is shown.

An analytical option changes the statistical object, model, selection, weighting, reference, resampling procedure, or other evidence being produced.

This distinction should be explicit whenever changing the option could change the interpretation.

## 6. Statistical evidence before interpretation

The companions should preserve a visible distinction between:

```text
what was calculated
and
what it means
```

Examples of statistical evidence include:

```text
estimated effects
adjusted means
p-values
V-tests
frequencies
penalties
eigenvalues
coordinates
contributions
cos²
distances
cluster descriptions
confidence regions
```

Interpretation comes after the reader knows what these quantities represent.

Do not overclaim:

```text
statistical significance ≠ practical importance
association ≠ causality
non-significance ≠ equivalence
a two-dimensional map ≠ the complete structure
a cluster ≠ a natural category by definition
an estimated optimum ≠ a tested product
```

## 7. The complementary roles of SEDA and MEDA

The two companions share an editorial system but not an identical statistical identity.

### SEDA

SEDA provides access to methods designed specifically for sensory and consumer data.

The companion should therefore remain strongly anchored in:

```text
sensory task
experimental structure
product / stimulus
subject / consumer
attributes
terms
liking
individual maps or categorizations
```

Its main analyses currently include:

```text
QDA characterization
QDA multivariate representation with ellipses
CATA
JAR
Napping
Sorting
Preference Mapping
```

### MEDA

MEDA provides access to general exploratory multivariate methods.

The companion should therefore emphasize statistical objects such as:

```text
individuals
quantitative variables
categorical variables
modalities
contingency tables
groups of variables
active elements
supplementary elements
factorial dimensions
clusters
```

Its main methodological families include:

```text
PCA
CA
MCA
MFA
HCPC
```

### Complementarity

SEDA and MEDA should not duplicate one another unnecessarily.

When a SEDA workflow relies on a general multivariate method, the SEDA companion should explain what the reader needs for the sensory task and may point to the MEDA companion for a deeper treatment of the multivariate method.

Conversely, MEDA should explain the general method without trying to reproduce sensory-specific workflows that belong to SEDA.

## 8. A stable chapter architecture

The current SEDA companion already provides a strong practical structure. The common default chapter architecture is therefore:

```text
Introduction
↓
Understanding what happens under the hood
↓
Expected data structure
↓
Interface guide
↓
Step-by-step procedure
↓
Interpretation of results
↓
Worked example
↓
Practical tips
↓
In summary
```

When useful, add:

```text
From jamovi to R
```

This section should remain short and should explain the reproducible computational path rather than teach R programming.

A chapter may deviate from this architecture when the method genuinely requires it. Consistency is a tool for the reader, not a constraint imposed for its own sake.

## 9. Worked examples are part of the method

Each major analysis should contain at least one reproducible worked example using a validated dataset.

The example should show:

```text
why this analysis is appropriate
how the variables are assigned
which options matter
which outputs are worth reading first
how several pieces of evidence combine
what conclusion is justified
what conclusion would go too far
```

Do not narrate every number shown in the output.

The worked example should teach a transferable reading strategy.

## 10. From jamovi back to R

When the module exposes reproducible R code, the companion should use it as a bridge toward transparency and autonomy.

The purpose is not to turn every jamovi user into an R programmer.

The purpose is to make visible that:

```text
jamovi analysis
↔
R implementation
↔
statistical method
```

A short section may therefore identify:

```text
the underlying R package or function family
the main analytical arguments
the correspondence with the jamovi options
what the reader could reproduce or extend in R
```

Exact function names or arguments should be documented only after they have been validated against the current module.

## 11. Software truth and editorial truth

A software companion needs two distinct source hierarchies.

### Software truth

When documentation and the validated module disagree, the module wins.

Use this order:

```text
validated current module behavior
>
current module implementation / generated R code when relevant
>
companion description
```

This applies particularly to:

```text
menu paths
field names
option names
defaults
conditions under which outputs appear
output names
available data outputs
R Code behavior
```

### Editorial truth

For the companion manuscript itself, use:

```text
current local .qmd
>
current render
>
previous companion version
>
main book
>
chat memory
```

Previous versions are references, not sources of truth about the current software.

## 12. Stable knowledge versus version-dependent knowledge

Keep stable methodological knowledge in the main companion text.

Examples:

```text
what a PCA axis represents
why adjusted means may be needed
what active and supplementary elements mean
why CATA frequencies and associations differ
why JAR frequency and penalty answer different questions
what Napping consensus represents
```

Treat the following as version-dependent and verify them during revision:

```text
exact menu names
exact option labels
default values
current output names
current screenshots
current function signatures
current software versions
```

The companion should age around the method, not the other way around.

## 13. Conservative revision

For an existing companion chapter:

> Preserve what still works; revise what improves correctness, understanding, reproducibility, or practical use.

Do not rewrite merely for stylistic uniformity.

Classify changes as:

```text
SCIENTIFIC CORRECTION
PEDAGOGICAL CLARIFICATION
SOFTWARE UPDATE
INTERFACE UPDATE
EXAMPLE UPDATE
EDITORIAL SIMPLIFICATION
```

A software update should never silently alter the methodological interpretation.

## 14. Final test for every chapter

Before considering a chapter complete, the reader should be able to answer:

```text
Is this the right analysis for my question?

What structure must my data have?

What do the main interface fields mean statistically?

Which options actually change the analysis?

Which outputs should I read first?

What evidence do they contain?

What can I conclude?

What should I not conclude?

Can I reproduce the worked example?

Can I see how the jamovi analysis relates to R when this is useful?
```

If the chapter answers these questions clearly, additional detail requires a reason.

## 15. Final principle

> The companion is successful when the interface becomes easier to use because the analysis has become easier to understand.
