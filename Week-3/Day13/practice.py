name = input("Enter your name: ")

for i in name:
    print(i)


# List
students = ["Ammar", "Khalid", "Meshal", "Ahmed"]
print(students)        # list
print(students[0])     # ammar
print(type(students))  # type


colors = ["red", "green", "blue"]
print(colors)      # list
print(colors[0])   # first element
print(colors[-1])  # last element
print(colors[5])   # IndexError: list index out of range


numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # [20, 30, 40]
print(numbers[:3])   # [10, 20, 30]
print(numbers[::2])  # [10, 30, 50]
print(numbers[::-1])  # [50, 40, 30, 20, 10]


tasks = ["Plan", "code"]

tasks[0] = "design"  # Overwrite the first element
tasks.append("test")
tasks.insert(1, "review")

print(tasks)


scores = [88, 72, 95, 81]

scores.remove(72)
last = scores.pop()  # remove the last element, save it in last variable
scores.sort()

print(scores)
print(last)


students = ["Ammar", "Khalid", "Meshal"]

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
print(matrix[0])
print(matrix[1][2])  # 6
print(matrix[0][4])  # out of range


locations = (24.7136, 46.6753)

print(locations[0])
print(locations[-1])

# locations[0] = 25  # TypeError


student = ("Ammar", 22, "python", "male", "female")

name, age, course, *other = student

print(name)
print(age)
print(course)


# dictionary of unique values No Duplicates
skills = {"python", "java", "python", }

skills.add("c++")

print(skills)
print("Git" in skills)
print(len(skills))


backend = {"python", "Django", "SQL"}
frontend = {"HTML", "CSS", "JS", "SQL"}

fullstack = (backend | frontend)  # union
print(fullstack)

fullstack = (backend & frontend)  # intersection
print(fullstack)

# difference - العناصر الموجودة في backend وليست في frontend → python, Django.
fullstack = (backend - frontend)
print(fullstack)


student = {
    "name": "Ammar",
    "age": 22,
    "course": "python",
}

print(student["name"])

student = {"name": "Ammar", "score": 90}

student["score"] = 95   # overwrite
student["grade"] = "A"  # add a new key

email = student.get("email", "Not set")
grade = student.pop("grade")  # remove the key and return the value

print(student)


students = {"name": "Sara", "score": 95}

for key in students:
    print(key)

for key, value in students.items():  # .items gave key and value
    print(key, value)


names = ["Sara", "Omar"]
skills = {"Python", "java"}
students = {"name": "Sara", "score": 95}

print(len(names))
print("Python" in skills)
print("name" in students)


students = [
    {"name": "Sara", "score": 95},
    {"name": "Omar", "score": 88},
]

for student in students:
    print(student["name"], student["score"])
