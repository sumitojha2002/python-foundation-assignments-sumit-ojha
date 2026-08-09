"""
Exercise: Student Score Dictionary
Student: Sumit Ojha
Day: 2
"""

# Input
student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}


# Calculation
atleast_60 = {student: marks for student,marks in student_scores.items() if student_scores[student] >= 60}
highest_score =  max(student_scores.values())
highest_scoreing_student = {key:value for key,value in student_scores.items() if value == highest_score}
calculate_avg = sum(student_scores.values())/len(student_scores)

# Output
print("\n\nStudent names and there scores: ")
for key,value in student_scores.items():
    print(f"name:{key} score: {value}")
print("\n")

print(f"Student who scored atleast 60: {atleast_60}")
print(f"Student with highest score: {highest_scoreing_student}")
print(f"Avg score : {calculate_avg:.2f}")