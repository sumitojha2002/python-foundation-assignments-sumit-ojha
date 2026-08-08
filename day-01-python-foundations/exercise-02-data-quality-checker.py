"""
Exercise : Data Quality Checker
Student: Sumit Ojha
Day: 1
"""

# Input values
total_rows = 2000
missing_rows = 120
dublicate_rows = 30

# Calculations
problematic_rows = missing_rows + dublicate_rows
problem_percentage = problematic_rows / total_rows * 100

if problem_percentage <= 2.0 :
    classification = "Excellent"
elif problem_percentage > 2.0 and problem_percentage <= 5.0:
    classification = "Acceptable"
else:
    classification = "Needs Cleaning"

# Output
print(f"Total rows: {total_rows}")
print(f"Problematic rows: {problematic_rows}")
print(f"Problem percentage: {problem_percentage:.2f} %")
print(f"Classification: {classification}")