class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)
        else:
            print("Invalid score")

    def average(self):
        if len(self.scores) == 0:
            return 0

        return sum(self.scores) / len(self.scores)

class Course:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f"Name: {student.name}, Scores: {student.scores}, Average: {student.average()}")


student1 = Student("Sara")
student2 = Student("Omar")

student1.add_score(90)
student1.add_score(95)

student2.add_score(80)
student2.add_score(85)

course = Course()

course.add_student(student1)
course.add_student(student2)

course.display_students()

