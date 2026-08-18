# Write to a CSV file
from pathlib import Path
import csv

with open("students.csv", "w",
          encoding="utf-8", newline="") as file:

    writer = csv.writer(file)
    writer.writerow(["name", "course"])
    writer.writerow(["Sara", "Python"])
    writer.writerow(["Ali", "Django"])


# Json preserves lists and dictionaries
import json

students = [
    {"name": "Sara", "score": 92},
    {"name": "Ali", "score": 85}
]

with open("student.json", "w", encoding="utf-8") as file:
    # dump the data(write)
    json.dump(students, file, indent=2)  # indent=2 for better formatting

with open("student.json", "r", encoding="utf-8") as file:
    # load the data(read)
    loaded = json.load(file)

print(loaded[0]["name"])


# try and except define a failure path
try:
    score = int(input("Enter a score: "))
except ValueError:
    print("Enter a whole number")

print("Program continues")


# cahtch the specific file failure you expect

try:
    text = Path("students.txt").read_text(encoding="utf-8")

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Student file cannot be read")


# else and finally run if the try runs without error

path = Path("students.txt")

try:
    text = path.read_text(encoding="utf-8")

except OSError as error:
    print("Load failed:", error)

else:
    print(text)
finally:  # runs no matter what happens
    print("Load attempted finished")


# raise reject
def validate_score(score):
    if not 0 <= score <= 100:
        #   raise to stop the program
        raise ValueError("Score must be between 0 and 100")
    return score


try:
    score = validate_score(120)

except ValueError as error:
    print(error)


# custom exception express domain failure
class StudentNotFoundError(Exception):
    pass


def finde_student(name, students):
    for student in students:
        if student["name"] == name:
            return student
    raise StudentNotFoundError(name)


students = [{"name": "Sara"}]

try:
    print(finde_student("Ali", students))
except StudentNotFoundError as error:
    print("Missing student:", error)
