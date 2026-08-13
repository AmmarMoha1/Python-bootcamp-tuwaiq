
from copy import deepcopy
students = [
    {"name": "Sara", "score": [90, 80, 85]},
    {"name": "Omar", "score": [85, 90, 95]},
    {"name": "Ahmed","score": [30, 55, 50]},
]

avg_students = [
    {
        "name": student["name"],
        "average": sum(student["score"]) / len(student["score"])
    }
    for student in students
]

filter_student = [
    student
    for student in avg_students
    if student["average"] >= 60
]

rep_index = {
    student["name"]: student
    for student in filter_student
}

backup = deepcopy(rep_index)

rep_index["Ahmed"] = {
    "name": "Ahmed",
    "average": 100
}

print(rep_index)
print(backup)
