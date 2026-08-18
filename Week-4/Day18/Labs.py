# Lab 1
class Ticket:
    def __init__(self, name, status = "Open"):
        self.name = name
        self.status = status

    def newStatus(self, status):
        self.status = status


myTicket1 = Ticket("1000", "In-Progress")
myTicket2 = Ticket("1001", "Pendig")


print(myTicket1.status)
print(f"Ticket ID: {myTicket2.name} is {myTicket2.status}")


# Lab 2
class Greeter:
    def __init__(self, message):
        self.message = message

    def greet(self, user):
        self.user = user 

        return(f"Hello {user}, {self.message}")

myGreet = Greeter("Welcome to Tuwaiq")
print(myGreet.greet("Ammar"))


# Lab 3 
class Welcome:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome {self.name}")


students = [
    Welcome("Sara"),
    Welcome("Mohammed"),
    Welcome("Khadijh")
]

for student in students:
    student.welcome()


# Lab 4
from pathlib import Path

path = Path("home") / "students" / "students.txt"

path.mkdir(parents=True, exist_ok=True)

print(path.is_dir())
print(path.suffix)
print(path.name)
print(path.is_file())

path.write_txt("Welcome to class", encoding="utf-8")
