# Companion Method Mapping — SEDA and MEDA

## 1. Purpose

This document provides the common methodological map for the SEDA and MEDA companions.

Its purpose is to prevent three problems:

```text
methods documented as isolated menu entries
SEDA and MEDA duplicating the same methodological explanations
documentation drifting away from the current modules
```

The map connects:

```text
analytical question
↓
data structure
↓
statistical method
↓
jamovi module
↓
statistical evidence
↓
R ecosystem
↓
companion chapter
```

It should remain compact and should be updated only when the overall understanding of the companions changes.

## 2. Common division of roles

### SEDA

SEDA is the sensory- and consumer-specific layer.

It is appropriate when the analysis depends on a sensory task or experimental structure such as:

```text
QDA ratings
CATA checking data
JAR responses
Napping coordinates
free-sorting categorizations
liking linked to a product space
```

### MEDA

MEDA is the general exploratory multivariate layer.

It is appropriate when the main statistical object is:

```text
a quantitative multivariate table
a contingency table
categorical variables
groups of variables
a factorial representation
a clustering problem in factorial space
```

### Combined workflows

Some analyses naturally use both layers.

The clearest current example is preference mapping:

```text
MEDA
construct or inspect the product representation space
↓
SEDA
model liking in that space
```

The companions should make such transitions explicit rather than pretending that each module is a self-contained statistical universe.

## 3. SEDA map

### 3.1 QDA — Characterization of the stimulus space

**Main question**

```text
Which sensory attributes differentiate the stimuli?
How is each stimulus characterized relative to the reference profile?
```

**Data structure**

```text
one row per evaluation
stimulus identifier
subject identifier
numeric sensory attributes
```

**Core statistical ideas**

```text
attribute-by-attribute modelling
stimulus effect
subject effect
global selection of discriminating attributes
stimulus-by-stimulus characterization
adjusted means
reference profile
positive and negative characterization
```

**Main evidence**

```text
p-values
V-tests
coefficients / departures from reference
adjusted means
```

**R ecosystem**

```text
SensoMineR and supporting R model functions
```

**MEDA relationship**

This analysis provides sensory profiles that can later be represented using general multivariate methods such as PCA.

---

### 3.2 QDA — Multivariate representation with ellipses

**Main question**

```text
How are the stimuli organized in the sensory space?
How stable are their positions with respect to panel composition?
```

**Data structure**

```text
repeated sensory evaluations
stimulus identifier
subject identifier
numeric sensory attributes
```

**Core statistical ideas**

```text
selection of sensory attributes
correction / accounting for subject effects
product sensory profiles
PCA
supplementary projected positions
resampling of subjects / virtual panels
confidence regions
product comparison
axis description
```

**Main evidence**

```text
factorial coordinates
eigenvalues / inertia
attribute representation
automatic dimension descriptions
resampled positions
confidence ellipses
product comparison statistics
```

**R ecosystem**

```text
SensoMineR
FactoMineR
```

**MEDA relationship**

PCA foundations should be treated more fully in the MEDA companion. The SEDA chapter should emphasize what is specific to sensory profile construction and panel resampling.

---

### 3.3 CATA — Analysis of checked terms

**Main question**

```text
Which terms are specifically associated with each stimulus?
How do stimuli differ in their checking profiles?
```

**Data structure**

```text
individual CATA responses
stimulus identifier
binary checked terms
```

**Core statistical ideas**

```text
aggregation into a stimulus × term contingency table
frequency versus association
stimulus characterization
Correspondence Analysis
optional clustering
```

**Main evidence**

```text
checking frequencies
characterization statistics
V-tests / p-values where provided
factorial geometry
cluster descriptions
```

**R ecosystem**

```text
SensoMineR / sensory preparation where applicable
FactoMineR for CA and clustering components
```

**MEDA relationship**

The SEDA companion should explain the CATA-specific construction and interpretation. The MEDA companion should provide the deeper general treatment of Correspondence Analysis.

---

### 3.4 JAR — Defect and penalty analysis

**Main question**

```text
Which deviations from the JAR reference occur for each product?
Which deviations are associated with lower liking?
```

**Data structure**

```text
product identifier
consumer identifier when required by the dataset
JAR variables
liking variable(s)
```

**Core statistical ideas**

```text
JAR as reference
recoding of non-JAR levels as deviations / defects
defect frequencies
product-specific defect characterization
factorial representation of defects where available
penalty calculation
```

**Main evidence**

```text
frequency of deviations
product specificity
characterization statistics
penalty magnitude
product-specific penalty displays
```

**Interpretative rule**

Always distinguish:

```text
frequency of a deviation
from
hedonic consequence of a deviation
```

**R ecosystem**

```text
SensoMineR and supporting R methods
```

**MEDA relationship**

General CA concepts may be cross-referenced when a defect profile map is interpreted.

---

### 3.5 Napping — Consensus representation

**Main question**

```text
What common product structure emerges from individual projective maps?
How consensual are the individual configurations?
```

**Data structure**

```text
products as rows
groups of two coordinates per subject
optional supplementary coordinates or information
```

**Core statistical ideas**

```text
one X/Y group per subject
MFA on grouped coordinates
unstandardized within-group logic for Napping
consensus / compromise
subject or group representation
supplementary information
automatic dimension description
optional clustering
```

**Main evidence**

```text
stimulus coordinates
subject / group representation
eigenvalues
dimension descriptions
supplementary information
clusters
```

**R ecosystem**

```text
FactoMineR
SensoMineR where sensory-specific preparation is involved
```

**MEDA relationship**

The MEDA companion should provide the general MFA framework. The SEDA chapter should explain the special structure of Napping data and why the groups are pairs of coordinates.

---

### 3.6 Sorting — Analysis of categorization

**Main question**

```text
What product structure emerges from individual free-sorting partitions?
Which categorizations and verbal information help explain this structure?
```

**Data structure**

```text
products as statistical individuals
one categorical variable per subject / sorting partition
optional verbal information
```

**Core statistical ideas**

```text
preservation of individual categorizations
MCA
rare-category ventilation when used
product, category, and variable representations
supplementary textual description
dimension description
optional clustering
```

**Main evidence**

```text
stimulus coordinates
category coordinates
variable / subject representation
eigenvalues
dimension descriptions
textual characterizations
clusters
```

**R ecosystem**

```text
FactoMineR
```

**MEDA relationship**

The MEDA companion should provide the general MCA foundations. The SEDA chapter should focus on why the raw individual categorizations are the relevant MCA structure for sorting.

---

### 3.7 Hedonic data — Preference Mapping

**Main question**

```text
How is liking related to position in an existing product space?
Which areas of the space are predicted to be preferred by more consumers?
```

**Data structure**

```text
existing product coordinates
individual liking variables
```

**Core statistical ideas**

```text
representation space constructed upstream
one preference model per liking variable / consumer as implemented
preference response surface
predicted favorable areas
limits of extrapolation
```

**Main evidence**

```text
product positions
fitted preference relationships
preference surface
proportion or level of predicted favorable response represented by the map
```

**R ecosystem**

```text
SensoMineR
FactoMineR or other validated upstream method for the product space
```

**MEDA relationship**

Strong combined workflow:

```text
MEDA PCA
→ construct / inspect product space
→ SEDA Preference Mapping
```

The SEDA chapter should not reteach PCA in full.

## 4. MEDA map

### 4.1 PCA — Principal Component Analysis

**Main question**

```text
How can a quantitative multivariate data table be represented with fewer dimensions while preserving its main structure?
```

**Data structure**

```text
individuals × quantitative variables
optional supplementary individuals
optional supplementary quantitative or categorical information where supported
```

**Core statistical ideas**

```text
centering
standardization when chosen
factorial axes
inertia / eigenvalues
coordinates
variable relationships
contributions
cos²
active versus supplementary information
```

**Main evidence**

```text
eigenvalues
individual coordinates
variable coordinates / correlations
contributions
cos²
supplementary projections
```

**SEDA relationship**

PCA is an important upstream or embedded component of several sensory workflows, including QDA product-space representation and preference mapping.

---

### 4.2 CA — Correspondence Analysis

**Main question**

```text
How can associations between row and column profiles of a contingency table be represented geometrically?
```

**Data structure**

```text
contingency table
rows × columns of non-negative frequencies
```

**Core statistical ideas**

```text
row profiles
column profiles
reference frequencies
chi-square geometry
inertia
row / column coordinates
contributions
quality of representation
```

**Main evidence**

```text
profile deviations
factorial coordinates
eigenvalues / inertia
contributions
cos² or equivalent quality indicators when provided
```

**SEDA relationship**

CA supports deeper understanding of CATA and, when used, JAR defect-profile representations.

---

### 4.3 MCA — Multiple Correspondence Analysis

**Main question**

```text
How can relationships among several categorical variables be summarized in a factorial space?
```

**Data structure**

```text
individuals × categorical variables
modalities
optional supplementary variables or individuals where supported
```

**Core statistical ideas**

```text
categorical profile geometry
modalities
rare categories / ventilation when relevant
factorial axes
individual and modality coordinates
contributions
quality of representation
supplementary information
```

**Main evidence**

```text
eigenvalues
individual coordinates
modality coordinates
variable information
contributions
cos² / representation quality where provided
```

**SEDA relationship**

MCA is the general multivariate foundation of the SEDA Sorting analysis.

---

### 4.4 MFA — Multiple Factor Analysis

**Main question**

```text
How can several groups of variables describing the same individuals be analyzed jointly without allowing the largest or most variable group to dominate the representation?
```

**Data structure**

```text
same individuals described by several predefined groups of variables
group types defined according to the analysis
optional supplementary groups
```

**Core statistical ideas**

```text
group structure
within-group analysis
balancing / group weighting
compromise representation
partial representations
group relationships
active versus supplementary groups
```

**Main evidence**

```text
compromise coordinates
group contributions / relationships
partial points
factorial dimensions
eigenvalues
supplementary group projections
```

**SEDA relationship**

MFA is the general multitable foundation of SEDA Napping, where each subject contributes a pair of coordinates.

---

### 4.5 HCPC — Hierarchical Clustering on Principal Components

**Main question**

```text
Can the multivariate structure be summarized by a small number of homogeneous groups?
```

**Data structure**

```text
factorial coordinates derived from a validated multivariate analysis
```

**Core statistical ideas**

```text
distance in retained factorial space
hierarchical clustering
choice / suggestion of partition
cluster consolidation where implemented
cluster characterization
```

**Main evidence**

```text
dendrogram / partition information
cluster membership
cluster positions
characteristic variables or modalities
characteristic individuals where provided
```

**Interpretative rule**

A cluster depends on:

```text
the input space
the retained dimensions
the distance / algorithmic choices
the chosen partition
```

It should not be described as a natural category by definition.

**SEDA relationship**

Clustering can complement several SEDA analyses after a factorial representation has been constructed.

## 5. Recurring concepts and their primary home

To reduce duplication, some concepts should have a primary detailed treatment.

| Concept | Primary companion home | Secondary use |
|---|---|---|
| Product / subject effects and adjusted means | SEDA QDA | SEDA QDA ellipses |
| Factorial axes, inertia, contributions, cos² | MEDA PCA | CA, MCA, MFA, SEDA factorial chapters |
| Contingency-table geometry | MEDA CA | SEDA CATA, JAR where applicable |
| Categorical factorial geometry | MEDA MCA | SEDA Sorting |
| Group balancing and compromise | MEDA MFA | SEDA Napping |
| Factorial-space clustering | MEDA HCPC | SEDA CATA, Napping, Sorting where applicable |
| Panel resampling and product-position uncertainty | SEDA QDA ellipses | — |
| Frequency versus specific association | SEDA CATA | SEDA JAR, MEDA CA |
| Frequency versus hedonic penalty | SEDA JAR | — |
| Preference modelling in an existing space | SEDA Preference Mapping | MEDA PCA provides upstream space |

Primary home does not mean exclusive home. Other chapters should provide the minimum reminder needed for an autonomous reading.

## 6. Cross-companion workflow map

### QDA product space

```text
SEDA
sensory-specific modelling and adjusted profiles
↓
PCA geometry
↓
MEDA concepts can deepen the reading of axes, contributions, cos², and supplementary elements
```

### CATA

```text
SEDA
construct and characterize stimulus × term profiles
↓
CA
↓
MEDA companion for general correspondence-analysis geometry
```

### Napping

```text
SEDA
individual projective maps
↓
MFA with one coordinate pair per subject
↓
MEDA companion for general MFA concepts
```

### Sorting

```text
SEDA
individual categorizations
↓
MCA
↓
MEDA companion for general MCA concepts
```

### Preference Mapping

```text
MEDA
construct / inspect representation space
↓
SEDA
fit preference models and construct preference surface
```

## 7. Relationship with the main book

The main book and the companions should not duplicate one another.

### Main book

Primary role:

```text
sensory / consumer question
statistical reasoning
R implementation
interpretation
methodological progression
```

### SEDA / MEDA companions

Primary role:

```text
same method through jamovi
data requirements
interface fields and options
current outputs
worked example
practical interpretation
bridge back to R
```

A companion may provide more detailed interface guidance than the book.

The book may provide a more extensive methodological argument than the companion.

## 8. Maintenance rule

Update this mapping only when one of the following changes:

```text
a method is added or removed from a companion
a method changes conceptual role
a new cross-module workflow becomes important
the primary location of a recurring explanation changes
a validated implementation reveals that the documented statistical architecture was wrong
```

Do not update this file for minor wording or interface-label changes.

Those belong in the relevant chapter or state file.

## 9. Final principle

> SEDA explains sensory-specific analysis. MEDA explains general multivariate structure. The companions meet where the analytical workflow genuinely meets.
