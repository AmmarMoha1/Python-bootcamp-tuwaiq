# practice
students = [
    {"name": "Ammar", "score": (90, 80, 55), "skills": {
        "Python", "Django", "SQL"}},
    {"name": "Khalid", "score": (80, 70, 65), "skills": {"HTML", "CSS", "JS"}},
    {"name": "Meshal", "score": (70, 90, 88), "skills": {"HTML", "CSS", "JS"}},
    {"name": "Ahmed", "score": (60, 80, 75), "skills": {"HTML", "CSS", "JS"}},
]
counter = 0
for student in students:
    average = (student['score'][0] + student['score'][1] +
               student['score'][2]) / len(student['score'])
    counter += 1
    student['skills'].add("Git")
    print(f"Student {counter}")
    print(f"Name: {student['name']}")
    print(f"Score: {student['score']}")
    print(f"Average: {average}")
    print(f"Skills: {student['skills']}")
    print("-----------------------")
