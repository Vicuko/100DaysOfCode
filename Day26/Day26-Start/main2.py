import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {name:random.randint(1,100) for name in names}

passed_students = {name:"Passed" for name,grade in students_scores.items() if grade > 49}

