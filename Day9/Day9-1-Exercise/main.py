student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = dict()

# TODO-2: Write your code below to add the grades to student_grades.👇
for key, value in student_scores.items():
    grade = None
    if value <= 70:
        grade = "Fail"
    elif value <= 80:
        grade = "Acceptable"
    elif value <= 90:
        grade = "Exceeds Expectations"
    else:
        grade = "Outstanding"
    student_grades[key] = grade

# 🚨 Don't change the code below 👇
print(student_grades)
