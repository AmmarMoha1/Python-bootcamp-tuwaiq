
from copy import deepcopy
numbers = range(1_000_000)

total = sum(

    number ** 2
    for number in numbers

)

print(total)


items = ["Python", "Git"]
items.append("Django")

name = "sara"
name = name.title().strip()

print(id(items))
print(id(name))


original = ["Python", "Git"]
alias = original

alias.append("Django")

print(original)
print(id(original))
print(alias)
print(id(alias))
print(original is alias)


original = ["Python", "Git"]
clone = original.copy()

clone.append("Django")

print(original)  # ['Python', 'Git'] #if there is a list it will be mutable
print(id(original))
print(clone)  # ['Python', 'Git', 'Django']
print(id(clone))
print(original is clone)  # False


# Shallow Copy
original = [["Sara", 90], ["Omar", 80]]
clone = original.copy()

clone[0][1] = 95

print(original)
print(id(original))
print(clone)
print(id(clone))
print(original[0] is clone[0])  # True


# Deep Copy

original = [["Sara", 90], ["Omar", 85]]
clone = deepcopy(original)

clone[0][1] = 95

print(original)
print(id(original))
print(clone)
print(id(clone))
print(original[0] is clone[0])  # False


names = ["Sara", "Omar", "Ahmed"]

# searches items one by one O(n)
print("Ahmed" in names)

name_set = set(names)

# Average membership time O(1)
print("Ahmed" in name_set)


students = [
    {"id": 101, "name": "Sara"},
    {"id": 102, "name": "Omar"},
]

studnets_by_id = {
    student["id"]: student
    for student in students
}

print(studnets_by_id[102]["name"])
