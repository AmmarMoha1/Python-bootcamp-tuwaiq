from pathlib import Path
import json

class InvalidStudentError(Exception):
    pass

data_dir = Path("data")
data_dir.mkdir(parents=True, exist_ok=True)

file_path = data_dir / "students.json"

def save_students(students):
    with open(file_path, "w") as file:
        json.dump(students, file, indent=2)

def load_students():
    try:
        with open(file_path, "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        print("Students file was not found.")
        
    except json.JSONDecodeError:
        print("The JSON file is invalid.")

    # Validate every student
    for student in students:

        if not isinstance(student, dict):
            raise InvalidStudentError("Student record must be a dictionary.")

        name = student.get("name")
        score = student.get("score")

        if not isinstance(name, str) or not name.strip():
            raise InvalidStudentError("Invalid student name.")

        if not isinstance(score, (int, float)):
            raise InvalidStudentError("Invalid student score.")

    return students


# Example data
students = [
    {"name": "Ahmed", "score": 90},
    {"name": "Sara", "score": 85},
    {"name": "Omar", "score": 95}
]

save_students(students)

# Load the students
try:
    loaded_students = load_students()
    print("Students loaded:")
    print(loaded_students)

except InvalidStudentError as error:
    print(f"Invalid student: {error}")

