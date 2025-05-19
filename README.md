# education-analytics-dashboard
This project is currently being created. It is part of my learning portfolio. This dashboard is used to analyze student performance trends and identify at-risk groups. I focused on English language learners in a simulated high school environment.
# Education Analytics Dashboard (DRAFT - BETA - In Progress)

## Objective
Analyze and visualize student performance data to uncover patterns and support data-driven decisions in a secondary school setting.

## Project Structure
- `data/`: Simulated dataset files (CSV)
- `notebooks/`: Jupyter notebooks for data exploration and analysis
- `images/`: Visualizations and output charts
- `app.py`: Streamlit dashboard script
- `README.md`: Project overview and instructions

## Tools & Libraries
- Python 3.x
- pandas
- numpy
- seaborn
- matplotlib
- streamlit

## Next Steps
1. Create simulated student data and store it in `data/student_performance.csv`
2. Build an initial notebook to explore the data and generate insights
3. Develop a Streamlit dashboard in `app.py`
4. Include key visuals in the `images/` folder

---

# app.py (Starter Template for Streamlit Dashboard)

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
def load_data():
    return pd.read_csv("data/student_performance.csv")

# Streamlit app
st.title("Education Analytics Dashboard")
st.write("Explore student performance trends and insights")

# Load and display data
data = load_data()
st.dataframe(data.head())

# Plot: Score Distribution
st.subheader("Test Score Distribution")
fig, ax = plt.subplots()
sns.histplot(data['test_score'], kde=True, ax=ax)
st.pyplot(fig)

# More charts and filters coming soon...
