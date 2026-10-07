# Analysis Preregistration

## Research question

Is weekly study time associated with students' final mathematics grade?

## Hypotheses

Null hypothesis (H₀): There is no significant association between weekly study time and students' final mathematics grade.

Alternative hypothesis (H₁): There is a significant association between weekly study time and students' final mathematics grade.

## Population, sample, and exclusions

Target population: Students represented in the UCI Student Performance Mathematics dataset.

Unit of analysis: Individual student.

Sample: All student records in the dataset with valid values for studytime and G3.

Inclusion rules: Students with valid values for studytime and G3 will be included.

Exclusion rules: Records with missing or invalid studytime or G3 values will be excluded.

Stopping rule: The complete eligible dataset will be used for the analysis.

## Variables and measures

Outcome: G3 (final mathematics grade), measured on a 0–20 scale.

Predictor: studytime (weekly study-time category).

Controls: No control variables will be used in the primary analysis.

Transformations: studytime will be treated as an ordinal variable. G3 will be treated as a numerical variable. No transformation will be applied to G3.

Missing-data handling: Records with missing studytime or G3 values will be excluded. No missing values will be imputed.

## Analysis plan

Primary analysis: A Kruskal-Wallis H test will be used to test whether final mathematics grades (G3) differ across the four studytime categories.

Secondary analysis: Spearman rank correlation will be used to measure the association between studytime and G3.

Significance level: α = 0.05.

Effect size: An appropriate effect size for the Kruskal-Wallis test will be reported.

Uncertainty intervals: 95% confidence intervals will be reported where applicable.

Robustness check: The Spearman rank correlation will be used as a secondary check of the relationship between studytime and G3.

Visualization: Boxplots will be used to compare G3 across the studytime categories.

## Deviations

No deviations from this preregistered analysis plan are planned. Any changes made after preregistration will be documented with the date, reason for the change, and its impact on the analysis.