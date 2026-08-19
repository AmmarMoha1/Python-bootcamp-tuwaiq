# Lab 1
class Student:

    __enrolled = True

    def __init__(self, name):
        self.name = name
        self.score = []

    def add_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.score.append(score)

    @property
    def enrolled(self):
        return self.__enrolled

    @enrolled.setter
    def enrolled(self, status):
        self.__enrolled = status

    @property
    def average(self):
        if not self.score:
            return 0
        return sum(self.score) / len(self.score)


student = Student("ammar")

student.add_score(100)
student.add_score(90)

print(student.average)

student.enrolled = False

print(student.enrolled)
print(student.score)


# Lab 2
class Food:

    def __init__(self, name):
        self.name = name

    def showname(self):
        return self.name


class Fruites(Food):

    def __init__(self, name, cal):
        super().__init__(name)
        self.cal = cal

    @staticmethod
    def stripName(name):
        return name.strip()


myFruit = Fruites("apple", 200)

print(myFruit.showname())
print(Fruites.stripName("    Fa  "))
