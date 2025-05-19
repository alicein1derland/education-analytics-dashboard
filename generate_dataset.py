import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of students
num_students = 600

# Grade levels and age means for more realistic age generation
grade_levels = np.repeat([7, 8, 9, 10, 11, 12], 100)
grade_age_mean = {7: 12.5, 8: 13.5, 9: 14.5, 10: 15.5, 11: 16.5, 12: 17.5}
ages = [int(np.clip(np.random.normal(grade_age_mean[grade], 0.5), 12, 18)) for grade in grade_levels]

# Simulate missing data helper
def insert_missing(data, missing_rate=0.05):
    mask = np.random.rand(len(data)) < missing_rate
    data = data.astype(object)
    data[mask] = None
    return data

# Generate data
data = {
    "Student ID": [f"S{i+1:03d}" for i in range(num_students)],
    "Grade Level": grade_levels,
    "Age": ages,
    "Gender": insert_missing(np.random.choice(["Male", "Female", "Other"], size=num_students, p=[0.48, 0.48, 0.04])),
    "Nationality": np.random.choice(["Thai", "Vietnamese", "Chinese", "Other"], size=num_students, p=[0.90, 0.03, 0.03, 0.04]),
    "English Proficiency Level": insert_missing(np.random.choice(["Beginner", "Intermediate", "Advanced"], size=num_students, p=[0.30, 0.40, 0.30])),
    "Attendance Rate": np.round(np.clip(np.random.normal(loc=85, scale=10, size=num_students), 0, 100), 1),
    "Test Score": np.round(np.clip(np.random.normal(loc=75, scale=10, size=num_students), 0, 100), 1),
    "Extracurricular Activities": np.random.choice(["Yes", "No"], size=num_students, p=[0.60, 0.40]),
    "Parental Education Level": insert_missing(np.random.choice(["High School", "Bachelor's", "Master's", "Doctorate"], size=num_students, p=[0.40, 0.40, 0.15, 0.05])),
    "Socioeconomic Status": np.random.choice(["Low", "Middle", "High"], size=num_students, p=[0.30, 0.50, 0.20]),
    "Learning Style": np.random.choice(["Visual", "Auditory", "Kinesthetic"], size=num_students, p=[0.40, 0.40, 0.20]),
    "Engagement Score": np.round(np.clip(np.random.normal(loc=70, scale=15, size=num_students), 0, 100), 1),
    "School ID": np.random.choice(["A", "B", "C"], size=num_students, p=[0.5, 0.3, 0.2])
}

# Create DataFrame
students_df = pd.DataFrame(data)

# Data Validation
assert students_df['Age'].between(12, 18).all(), "Age values are out of bounds!"
assert students_df['Attendance Rate'].between(0, 100).all(), "Attendance rates should be between 0 and 100!"
assert students_df['Test Score'].between(0, 100).all(), "Test scores should be between 0 and 100!"

# Display the first few rows of the dataset
print(students_df.head())

# Optionally, save to CSV
students_df.to_csv("students_dataset.csv", index=False)
