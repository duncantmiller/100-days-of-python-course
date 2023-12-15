student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

def grade_for(score):
    if score > 90:
        return "Outstanding"
    elif score > 80:
        return "Exceed Expectations"
    elif score > 70:
        return "Acceptable"
    else:
        return "Fail"

for key in student_scores:
    student_grades[key] = grade_for(student_scores[key])

# 🚨 Don't change the code below 👇
print(student_grades)
