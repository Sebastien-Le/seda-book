# Représentation multivariée de l'espace des stimuli

## 1. Introduction

Cette analyse est conçue pour les données de **Quantitative Descriptive Analysis (QDA)**, c'est-à-dire lorsque plusieurs sujets évaluent plusieurs stimuli à l'aide d'une liste fixe d'attributs sensoriels. Elle répond à deux questions complémentaires : **quels stimuli se ressemblent sensoriellement** et **cette proximité est-elle stable malgré la variabilité entre sujets** ? Son résultat central est une carte des stimuli enrichie d'**ellipses**, qui visualisent non seulement la position des stimuli, mais aussi la robustesse de cette position face au rééchantillonnage du panel.

### Pourquoi ne pas utiliser une alternative standard ?

Une ACP appliquée directement aux données brutes risque de mélanger deux sources de variation : l'effet **stimulus** et l'effet **sujet**. Or, en analyse sensorielle, certains sujets notent systématiquement plus haut ou plus bas que les autres, ou utilisent l'échelle de façon plus ou moins large. Cette analyse tient compte de cette structure sujet/stimulus pour produire une représentation plus adaptée aux données QDA.

---

## 2. Comprendre ce qui se passe "sous le capot"

### 2.1 Sélection des attributs sensoriels

Avant de construire la carte, le module identifie les attributs qui discriminent suffisamment les stimuli. Cette sélection est pilotée par **p-value of the Stimulus effect (%)**. Plus le seuil est strict, plus la carte sera épurée ; plus il est large, plus la représentation sera exhaustive, mais parfois plus chargée. La valeur par défaut est **20 %**, ce qui en fait un bon point de départ pour l'exploration.

### 2.2 Correction de l'effet sujet

Une manière simple de comprendre l'étape suivante est de dire que l'analyse reconstruit des **profils sensoriels moyens par stimulus**, en tenant compte des différences entre sujets. Deux options interviennent ici :

- **Center by subject** corrige les différences de niveau moyen entre sujets ;
- **Scale by subject** corrige les différences d'amplitude d'utilisation de l'échelle.

L'objectif est d'éviter qu'un sujet très généreux, très sévère, ou très "étalé" dans ses réponses déforme artificiellement la carte des stimuli.

### 2.3 Analyse en composantes principales

Une **ACP** est ensuite réalisée sur le tableau des profils sensoriels ainsi obtenu. Elle produit la carte des stimuli, la carte des attributs sensoriels, les valeurs propres et la description automatique des dimensions. C'est cet espace factoriel qui sert ensuite de référence pour projeter les panels virtuels.

### 2.4 Panels virtuels et individus supplémentaires

Le point clé du module est l'usage du **rééchantillonnage**. En ACP, il est possible de distinguer les **individus actifs** — ceux qui servent à construire les axes — des **individus supplémentaires** — ceux qui sont projetés après coup, sans modifier les axes. C'est précisément ce mécanisme qui permet de construire les ellipses.

À chaque simulation, un sous-ensemble de sujets est tiré avec remise depuis le panel original, de nouveaux profils moyens de stimuli sont recalculés, puis projetés dans l'espace factoriel comme individus supplémentaires. La dispersion de ces projections autour de chaque stimulus est ensuite résumée par une ellipse.

Ces ellipses décrivent donc la variabilité de la **position moyenne des stimuli quand la composition du panel change**, et non la simple dispersion brute des notes individuelles.

> **Note de performance :** le calcul peut prendre quelques secondes, car il repose sur un grand nombre de panels virtuels. Pendant ce calcul, mieux vaut éviter de modifier d'autres options pour ne pas relancer inutilement la procédure.

### 2.5 Comparaison entre stimuli

Quand le nombre de sujets simulés est supérieur à 1, le module calcule aussi une comparaison entre paires de stimuli, présentée sous forme de matrice de **p-values**. Cette sortie complète la lecture visuelle des ellipses en ajoutant une mesure chiffrée de la distinction entre stimuli.

### 2.6 Description automatique des dimensions

Le module propose enfin une description automatique des axes, filtrée selon **Significance threshold (%)**. Elle aide à identifier quels attributs sont les plus associés à chaque dimension et à donner un sens sensoriel aux axes.

---

## 3. Structure des données attendues

Les données doivent contenir :

- une colonne identifiant les **stimuli** ;
- une colonne identifiant les **sujets** ou **panélistes** ;
- plusieurs colonnes numériques correspondant aux **attributs sensoriels**.

Chaque ligne correspond à l'évaluation d'un stimulus par un sujet. Si un sujet évalue plusieurs fois un même stimulus (répétitions ou sessions), chaque évaluation doit apparaître sur une ligne distincte. Le module rejette explicitement l'analyse si les variables placées dans **Sensory Attributes** ne sont pas numériques.

Avant de lancer l'analyse dans jamovi, vérifiez dans l'onglet **Données** que :

- la variable destinée à **Stimulus Effect** est bien catégorielle ;
- la variable destinée à **Subject Effect** est bien catégorielle ;
- toutes les variables destinées à **Sensory Attributes** sont numériques.

---

## 4. Guide de l'interface

L'analyse apparaît dans le menu **SEDA > Fixed List of Attributes > Representation of the Stimulus Space**, avec le sous-titre **SensoMineR::panellipse**. L'interface comporte trois zones de dépôt de variables, une aide intégrée, puis trois menus repliables : **Graphic Options**, **Resampling Options** et **Numerical Indicators**.

### Variables à renseigner

#### Stimulus Effect

**Rôle :** identifie les stimuli à représenter sur la carte.
**Impact sur le calcul :** chaque modalité de cette variable devient un point moyen et, le cas échéant, une ellipse sur la carte.
**Conseil pratique :** utilisez des libellés clairs, car ils apparaîtront directement dans les graphiques.

#### Subject Effect

**Rôle :** identifie les sujets ou panélistes.
**Impact sur le calcul :** cette variable est indispensable pour corriger l'effet sujet et pour générer les panels virtuels utilisés dans le bootstrap.
**Conseil pratique :** vérifiez qu'un même sujet conserve exactement le même identifiant dans tout le fichier.

#### Sensory Attributes

**Rôle :** regroupe les attributs sensoriels utilisés pour construire l'espace factoriel.
**Impact sur le calcul :** seuls des attributs numériques sont acceptés ; le nombre de dimensions calculables dépend du nombre d'attributs retenus.
**Conseil pratique :** commencez par inclure tous les attributs sensoriels pertinents, puis affinez avec **p-value of the Stimulus effect (%)**.

---

### Option générale

#### Read me before running

**Rôle :** affiche un texte d'aide intégré dans les résultats.
**Impact sur le calcul :** aucun effet statistique.
**Conseil pratique :** laissez cette option cochée lors des premières utilisations. La valeur par défaut est **activée**.

---

### Standardization of the Sensory Attributes

#### Scale to unit variance

**Rôle :** standardise les attributs sensoriels avant l'ACP.
**Impact sur le calcul :** cochée, chaque attribut contribue sur une base comparable ; décochée, les attributs les plus dispersés influencent davantage la construction des axes.
**Conseil pratique :** laissez cette option cochée dans la plupart des analyses. Elle est **activée par défaut**.

---

### Selection of the Sensory Attributes

#### p-value of the Stimulus effect (%)

**Rôle :** fixe le seuil de sélection des attributs selon leur lien avec l'effet stimulus.
**Impact sur le calcul :** un seuil faible retient peu d'attributs et produit une carte plus lisible ; un seuil plus élevé retient davantage d'attributs et donne une vision plus large.
**Conseil pratique :** la valeur par défaut est **20 %**, bon point de départ pour explorer. Pour une version plus stricte, commencez à **5 %**.

---

### Graphic Options

#### Components to Plot — X-axis et Y-axis

**Rôle :** choisissent les dimensions affichées en abscisse et en ordonnée.
**Impact sur le calcul :** ne changent pas l'ACP elle-même, mais modifient le plan factoriel affiché. Les dimensions sélectionnées doivent exister dans l'analyse, sinon le module génère une erreur.
**Conseil pratique :** commencez avec **X-axis = 1** et **Y-axis = 2**, valeurs par défaut.

#### Individual variability around stimuli

**Rôle :** ajoute un graphique montrant la dispersion des évaluations individuelles autour de chaque stimulus.
**Impact sur le calcul :** n'ajoute pas une nouvelle analyse, mais une sortie graphique supplémentaire utile pour juger le consensus entre sujets.
**Conseil pratique :** activez cette option si vous souhaitez distinguer un stimulus consensuel d'un stimulus perçu plus diversement. La valeur par défaut est **désactivée**.

#### Variability around sensory attributes

**Rôle :** ajoute un graphique montrant la variabilité des attributs sensoriels sous rééchantillonnage.
**Impact sur le calcul :** fournit une sortie graphique utile pour juger la stabilité de l'interprétation des attributs.
**Conseil pratique :** activez cette option lorsque vous souhaitez commenter la robustesse des axes. La valeur par défaut est **désactivée**.

---

### Resampling Options

#### Number of subjects

**Rôle :** définit le nombre de sujets tirés dans chaque panel virtuel.
**Impact sur le calcul :** plus cette valeur est proche de l'effectif réel du panel, plus les panels simulés lui ressemblent et plus les ellipses ont tendance à être resserrées.
**Conseil pratique :** utilisez l'effectif réel du panel comme point de départ quand c'est possible. La valeur par défaut est **20**.

#### Number of panels

**Rôle :** fixe le nombre total de panels virtuels simulés.
**Impact sur le calcul :** plus ce nombre est grand, plus les ellipses sont stables d'une exécution à l'autre, mais le temps de calcul augmente.
**Conseil pratique :** **300** est un bon compromis pour commencer ; pour un rendu final, **500 ou plus** peut être utile. La valeur par défaut est **300**.

#### Threshold (%)

**Rôle :** définit le niveau utilisé pour tracer les ellipses.
**Impact sur le calcul :** un seuil faible produit des ellipses plus larges correspondant à un niveau de confiance plus élevé.
**Conseil pratique :** laissez **5 %** pour un premier essai. C'est la valeur par défaut.

#### Center by subject

**Rôle :** centre les réponses sujet par sujet.
**Impact sur le calcul :** corrige les différences de niveau moyen entre sujets et améliore souvent la comparabilité des profils.
**Conseil pratique :** laissez cette option cochée dans la quasi-totalité des analyses QDA. Elle est **activée par défaut**.

#### Scale by subject

**Rôle :** standardise les réponses sujet par sujet.
**Impact sur le calcul :** corrige les différences d'amplitude entre sujets, mais modifie plus fortement la structure initiale que le centrage seul.
**Conseil pratique :** laissez cette option décochée dans un premier temps. Elle est **désactivée par défaut**.

---

### Numerical Indicators

#### Significance threshold (%)

**Rôle :** définit le seuil de significativité pour la description automatique des dimensions.
**Impact sur le calcul :** plus le seuil est strict, plus la description automatique est sélective.
**Conseil pratique :** la valeur par défaut, **5 %**, convient bien à une première lecture.

#### Number of dimensions

**Rôle :** définit le nombre de dimensions à calculer et à décrire.
**Impact sur le calcul :** cette valeur est limitée par les dimensions effectivement calculables par l'ACP.
**Conseil pratique :** la valeur par défaut, **2**, est adaptée à une lecture initiale.

---

## 5. Procédure pas à pas

1. Ouvrez votre jeu de données dans jamovi.
2. Dans l'onglet **Données**, vérifiez que la variable stimulus est catégorielle, la variable sujet est catégorielle, et que les attributs sensoriels sont numériques.
3. Ouvrez **SEDA > Fixed List of Attributes > Representation of the Stimulus Space**.
4. Placez la variable stimulus dans **Stimulus Effect**.
5. Placez la variable sujet dans **Subject Effect**.
6. Placez tous les attributs sensoriels dans **Sensory Attributes**.
7. Laissez **Scale to unit variance** coché.
8. Réglez **p-value of the Stimulus effect (%)** à **20 %** pour une exploration initiale, ou à **5 %** pour une sélection plus stricte.
9. Conservez **X-axis = 1** et **Y-axis = 2**.
10. Laissez **Center by subject** coché et **Scale by subject** décoché au départ.
11. Réglez **Number of subjects** sur l'effectif du panel ou une valeur proche, laissez **Number of panels** à **300** et **Threshold (%)** à **5**.
12. Activez **Individual variability around stimuli** et/ou **Variability around sensory attributes** selon vos besoins.
13. Dans **Numerical Indicators**, gardez les valeurs par défaut pour un premier essai.
14. Lisez d'abord **Representation of the Stimuli with Ellipses**, puis **Eigenvalue Decomposition**, puis **Automatic Description of the Dimensions**.
15. Revenez ensuite sur les réglages pour tester la stabilité de vos conclusions.

---

## 6. Interprétation des résultats

### Representation of the Stimuli with Ellipses

C'est le graphique central du module. Chaque stimulus est représenté par un point moyen dans l'espace factoriel, entouré d'une ellipse. Les axes sont issus de l'ACP, et le pourcentage affiché sur chaque axe indique la part de variance expliquée.

| Situation observée | Lecture possible |
|---|---|
| Deux stimuli proches | Profils sensoriels similaires |
| Ellipses très chevauchantes | Différence peu robuste |
| Ellipse petite | Position stable selon les panels simulés |
| Ellipse grande | Position plus incertaine |
| Ellipses bien séparées | Différence plus robuste |

> **Point de vigilance :** les ellipses décrivent la variabilité de la position moyenne des stimuli sous rééchantillonnage du panel. Elles ne représentent pas directement la dispersion brute des notes individuelles.

### Representation of the Stimuli

Cette carte montre les positions relatives des stimuli sans mettre l'accent sur les ellipses. Elle est utile pour repérer rapidement les regroupements et les oppositions majeures entre stimuli.

### Representation of the Sensory Attributes

Cette carte montre les attributs sensoriels dans l'espace factoriel. On la lit selon trois repères simples :

- **la direction** : vers quels stimuli l'attribut "tire" la structure ;
- **la longueur** : plus un attribut est long, mieux il est représenté sur le plan ;
- **l'angle entre deux attributs** : petit angle = corrélation positive ; angle proche de 180° = opposition ; angle proche de 90° = quasi-indépendance.

C'est cette carte qui permet de donner un sens sensoriel aux axes.

### Individual variability around stimuli *(disponible uniquement si l'option est activée)*

Cette sortie montre la dispersion des évaluations individuelles autour du point moyen de chaque stimulus. Un nuage compact indique un fort consensus ; un nuage dispersé indique une perception plus hétérogène entre sujets.

### Variability around sensory attributes *(disponible uniquement si l'option est activée)*

Cette sortie montre la dispersion de la position des attributs sensoriels dans les panels virtuels. Un nuage compact signifie que l'attribut est stable ; un nuage dispersé indique que son interprétation est plus fragile et dépend davantage de la composition du panel.

### Eigenvalue Decomposition

Ce tableau donne, pour chaque dimension, la valeur propre, le pourcentage de variance expliqué et le pourcentage cumulé. Si les deux premières dimensions expliquent une grande part de la variance, la carte 2D résume bien les données. Dans le cas contraire, il est prudent d'explorer d'autres plans, par exemple Dim 1 / Dim 3.

### Automatic Description of the Dimensions

Cette sortie textuelle identifie les attributs les plus liés à chaque dimension, filtrés par **Significance threshold (%)**. Elle aide à nommer les axes de manière sensorielle et complète bien la carte des attributs.

### Product-by-product comparison table *(disponible uniquement si Number of subjects > 1)*

Cette matrice de p-values compare chaque paire de stimuli dans l'espace factoriel. Une p-value faible suggère une différence plus nette entre deux stimuli ; une p-value élevée suggère une proximité plus plausible. Ce tableau complète la lecture visuelle des ellipses, surtout lorsque leur chevauchement est difficile à interpréter à l'œil.

---

## 7. Exemple concret

Le jeu de données **sensochoc** est explicitement mentionné dans l'aide intégrée du module. Il permet de représenter **6 chocolats** évalués par **29 sujets**, avec un exemple où **choc2**, **choc5** et **choc6** présentent des ellipses qui se chevauchent, tandis que l'attribut **crunchy** apparaît plus variable que **cocoa aroma**.

### Réglages conseillés

| Option | Valeur |
|---|---|
| Stimulus Effect | variable stimulus |
| Subject Effect | variable sujet |
| Sensory Attributes | tous les attributs sensoriels |
| Scale to unit variance | Coché |
| p-value of the Stimulus effect (%) | 20 |
| X-axis / Y-axis | 1 / 2 |
| Number of subjects | 29 ou effectif réel du panel |
| Number of panels | 300 |
| Threshold (%) | 5 |
| Center by subject | Coché |
| Scale by subject | Décoché |
| Significance threshold (%) | 5 |
| Number of dimensions | 2 |

### Lecture plausible

Sur la carte avec ellipses, **choc2**, **choc5** et **choc6** apparaissent proches et leurs ellipses se chevauchent largement : on peut donc considérer que leur différenciation est peu robuste avec ce panel. À l'inverse, **choc1** est plus isolé, et la carte des attributs peut montrer qu'il se situe davantage du côté de *bitterness* et *cocoa aroma*. Le graphique de variabilité des attributs peut aussi révéler que *crunchy* est plus instable que *cocoa aroma*, ce qui invite à commenter ces attributs avec un niveau de confiance différent.

---

## 8. Conseils pratiques

- Commencez toujours avec **X-axis = 1** et **Y-axis = 2**.
- Laissez **Scale to unit variance** coché dans la plupart des cas.
- Utilisez **Center by subject** presque systématiquement.
- N'activez **Scale by subject** que si vous avez une bonne raison de penser que les sujets utilisent l'échelle avec des amplitudes très différentes.
- Commencez avec **300** panels simulés ; augmentez à **500 ou plus** pour une version finale plus stable.
- Réglez **p-value of the Stimulus effect (%)** entre **5 %** et **20 %** selon que vous cherchez une carte épurée ou plus exhaustive.
- N'interprétez jamais la carte des stimuli sans regarder aussi la carte des attributs.
- Ne concluez pas trop vite à une différence quand les ellipses se chevauchent fortement.
- Consultez **Product-by-product comparison table** pour compléter la lecture visuelle lorsque le chevauchement est ambigu.
- Si les deux premières dimensions résument peu de variance, explorez d'autres plans factoriels.

---

## 9. En résumé

Cette analyse produit une représentation multivariée des stimuli adaptée aux données QDA, en tenant compte de l'effet sujet dans la construction des profils sensoriels. Elle enrichit la carte factorielle classique par des ellipses obtenues par rééchantillonnage, ce qui permet d'évaluer la robustesse des positions observées. Elle montre donc non seulement **où se situent les stimuli**, mais aussi **avec quel degré de confiance on peut les y situer**.
