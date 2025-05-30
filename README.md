## Education Analytics Dashboard (In Progress)
**Started:** May 5, 2025 | **Part of my learning portfolio**

This project analyzes simulated student performance data from a secondary school environment (grades 7–12) in Northern Thailand. The dashboard explores trends affecting English language learners and provides visual tools to help educators and administrators understand and respond to those patterns.

## Background
Having worked as a teacher in Thailand for over six years, I often saw students—especially English language learners—struggle silently until it was too late to intervene. I created this dashboard to explore more efficient ways of identifying at-risk students early, using data as a lens to highlight those who might otherwise fall through the cracks.

## Mission Statement
The mission of this dashboard is to support educators in making proactive, data-informed decisions that improve outcomes for English language learners. By surfacing key performance trends and identifying at-risk groups, the tool aims to empower targeted, timely interventions in educational settings.

## Core Questions
* What are the prevailing performance trends over time?
* How is performance distributed across different grades or class sections?
* Which indicators are signaling that a student may be at risk?

## Project Structure
- `data/`: Simulated dataset files (CSV)
- `notebooks/`: Jupyter notebooks for data exploration and analysis
- `images/`: Visualizations and output charts
- `app.py`: Streamlit dashboard script
- `README.md`: Project overview and instructions

## Tools & Libraries
- Python 3.13
- pandas
- numpy
- seaborn
- matplotlib
- streamlit

## My Next Steps
1. Create simulated student data and store it in `data/student_performance.csv`
2. Build an initial notebook to explore the data and generate insights
3. Develop a Streamlit dashboard in `app.py`
4. Include key visuals in the `images/` folder

---
<!-- ## Design Decisions
<! ---
<! ## Installation
<! To install the required Python packages, run:

<! ```bash
<! pip install pandas numpy seaborn matplotlib streamlit

<! # app.py (Starter Template for Streamlit Dashboard)

<! import streamlit as st
<! import pandas as pd
<! import seaborn as sns
<! import matplotlib.pyplot as plt

<! # Load the data
<! def load_data():
<!     return pd.read_csv("data/student_performance.csv")

<! # Streamlit app
<! st.title("Education Analytics Dashboard")
<! st.subheader("Analyzing trends to identify at-risk English language learners")

<! # Load and display data
<! data = load_data()
<! st.dataframe(data.head())

<! # Plot: Score Distribution
<! st.subheader("Test Score Distribution")
<! fig, ax = plt.subplots()
<! sns.histplot(data['test_score'], kde=True, ax=ax)
<! st.pyplot(fig)
