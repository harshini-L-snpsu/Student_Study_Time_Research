import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kruskal, spearmanr

# Load the UCI Student Performance Mathematics dataset
data = pd.read_csv("raw/student-mat.csv", sep=";")

# Keep only the variables required for the preregistered analysis
data = data[["studytime", "G3"]].dropna()

# Create groups based on study time
groups = [
    group["G3"].values
    for _, group in data.groupby("studytime")
]

# Primary analysis: Kruskal-Wallis H test
statistic, p_value = kruskal(*groups)
# Effect size: epsilon-squared for Kruskal-Wallis
n = len(data)
k = data["studytime"].nunique()

epsilon_squared = (statistic - k + 1) / (n - k)

print(f"Epsilon-squared effect size: {epsilon_squared:.4f}")

# Secondary analysis: Spearman rank correlation
correlation, spearman_p = spearmanr(
    data["studytime"],
    data["G3"]
)

# Display results
print("Analysis completed successfully.")
print(f"Kruskal-Wallis H statistic: {statistic:.4f}")
print(f"Kruskal-Wallis p-value: {p_value:.4f}")
print(f"Spearman correlation: {correlation:.4f}")
print(f"Spearman p-value: {spearman_p:.4f}")

# Visualization: Boxplot of G3 across study-time categories
plt.figure(figsize=(8, 5))
data.boxplot(column="G3", by="studytime")
plt.title("Final Mathematics Grade by Weekly Study Time")
plt.suptitle("")
plt.xlabel("Weekly Study Time Category")
plt.ylabel("Final Mathematics Grade (G3)")
plt.tight_layout()

# Save the figure
plt.savefig("reports/studytime_g3_boxplot.png")
plt.close()

print("Boxplot saved to reports/studytime_g3_boxplot.png")