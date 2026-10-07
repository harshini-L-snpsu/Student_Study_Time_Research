# Student Study Time and Mathematics Performance

## Research Question

Is weekly study time associated with students' final mathematics grade?

## Dataset

The analysis uses the UCI Student Performance Mathematics dataset.

- Outcome: `G3` (final mathematics grade, 0–20)
- Predictor: `studytime` (weekly study-time category, 1–4)
- Unit of analysis: Individual student

## Statistical Analysis

### Primary Analysis

A Kruskal–Wallis H test was used to compare final mathematics grades across the four weekly study-time categories.

**H statistic:** 7.5789  
**p-value:** 0.0556  
**Epsilon-squared effect size:** 0.0117

At the α = 0.05 significance level, the Kruskal–Wallis result is not statistically significant.

The epsilon-squared effect size is small, indicating a weak difference in grades across the study-time categories.

### Secondary Analysis

A Spearman rank correlation was used to assess the monotonic association between weekly study time and final mathematics grade.

**Spearman correlation:** 0.1052  
**p-value:** 0.0367

This indicates a weak positive association that is statistically significant at α = 0.05.

### Visualization

A boxplot was created to compare final mathematics grades across the four weekly study-time categories.

The figure is saved as:

`reports/studytime_g3_boxplot.png`

## Conclusion

The primary Kruskal–Wallis analysis does not provide sufficient evidence at the 0.05 significance level to conclude that final mathematics grades differ across weekly study-time categories.

The secondary Spearman analysis indicates a weak positive association between study time and final grade.

The effect size for the Kruskal–Wallis test is small (ε² = 0.0117).

These results describe an association and do not establish a causal relationship between study time and mathematics performance.