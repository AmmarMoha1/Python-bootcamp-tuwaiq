class Student: 
    pass

print(Student)
print(type(Student))

#calling a class
student_one = Student()
student_two = Student()
print(student_one)
print(student_one is student_two)  #false

# __init__ Establishes the starting state of the object
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

student = Student("Sara", 90)

print(student.name)
print(student.score)


# self is a reference to the current instance
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}")

student = Student("Omar")
student.introduce()


# instance attributes belong to one object
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

sara = Student("Sara", 92)
omar = Student("Omar", 81)

sara.score = 95

print(sara.score)
print(omar.score)
print(omar is sara)  #false
print(isinstance(omar, Student))  #true


# class attributes are shared Default
class Student:
    academy = "Tuwaiq Academy"  #class attribute
    def __init__(self, name, ):
        self.name = name        #instance attribute

sara = Student("Sara")

print(Student.academy)
print(sara.academy)


#Instance methods Define Object Behavior
class Student:
    def __init__(self,name, score):
        self.name = name
        self.score = score

    def display_result(self):
        print(self.name, self.score)

student = Student("Sara", 92)
student.display_result()


#Class methods Define Class Behavior
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

counter = Counter()
counter.increment()
counter.increment()

print(counter.value) #2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(5, 3)

print(rectangle.area())  


#Method can protect valid states
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True

account = BankAccount(500)
print(account.withdraw(100))
print(account.balance)


#__str__ Gives and object a Readoble Descreption
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

# نتسخدم __str__ اذا بنطبع حاجه بدون ما نستدعي الميثود
    def __str__(self):
        return f"Name: {self.name}, Score: {self.score}"

student = Student("Sara", 95)
print(student)


# Each Instance keeps independent state
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

first = Counter()
second = Counter()

first.increment()
print(first.value)   #1
print(second.value)  #0


# Collection can store object
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

students = [
    Student("Sara"),
    Student("Omar"),
    Student("Lina")
]

print(students[1].name)

for student in students:
    print(student.greet())


class Student:
    pass

student = Student()

print(type(student))
print(type(student) is Student)
print(isinstance(student, Student))


#attribute access is public by default 
class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = score  #private "_" , but we can overwrite

student = Student("Sara", 95)

# student._score = 45    
print(student.name)
print(student._score) #accessible, but treated as internal


# a small class keeps data and behavior
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)

    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)

student = Student("Sara", [80, 90])
student.add_score(100)
print(student.name, student.average())