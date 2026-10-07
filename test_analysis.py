import pandas as pd
from scipy.stats import kruskal, spearmanr

# Load synthetic test data
data = pd.read_csv("tests/synthetic_data.csv")

# Check required columns
assert "studytime" in data.columns
assert "G3" in data.columns

# Run primary analysis
groups = [
    group["G3"].values
    for _, group in data.groupby("studytime")
]

statistic, p_value = kruskal(*groups)

# Run secondary analysis
correlation, correlation_p = spearmanr(
    data["studytime"],
    data["G3"]
)

# Expected output contracts
assert pd.notna(statistic)
assert pd.notna(p_value)
assert pd.notna(correlation)
assert pd.notna(correlation_p)

print("Synthetic data pipeline test PASSED")
print(f"Kruskal-Wallis p-value: {p_value:.4f}")
print(f"Spearman correlation: {correlation:.4f}")