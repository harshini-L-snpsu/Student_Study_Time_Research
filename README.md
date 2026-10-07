# Student Study Time Research

## Research Question

Is weekly study time associated with students' final mathematics grade?

## Dataset

This project uses the UCI Student Performance Mathematics dataset.

- Predictor: `studytime`
- Outcome: `G3`
- Study time categories: 1–4
- Final grade scale: 0–20

## Project Structure

```text
Student_Study_Time_Research/
├── notebooks/
│   └── analysis_notebook.ipynb
├── preregistration/
│   └── analysis_preregistration.md
├── raw/
│   └── student-mat.csv
├── reports/
│   ├── analysis_report.md
│   └── studytime_g3_boxplot.png
├── src/
│   └── analyze_data.py
├── tests/
│   ├── synthetic_data.csv
│   └── test_analysis.py
└── requirements.txt