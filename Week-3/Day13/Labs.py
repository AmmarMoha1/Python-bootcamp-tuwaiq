import math

# # Lab 1
# students = ["Sara", "mashaeal", "Dalal", "Taif"]

# for student in students:
#     print(student)


# itreable = enumerate(students) # (0, "Sara")
# print(next(itreable))


# # Lab 2
# set_col = {"Abdullah", "Nasser", "Dalal, mashaeal"}
# tuple_col = (11, 22, 33, 44, 55, 66)
# dict_col = {"name" : "Abdullah", "age" : 22, "has_car" : True}
# list_col = ["ABC", 333, (33, 44)]

# for c in dict_col.values():
#     print(type(c))  # <class 'str'> , <class 'int'> , <class 'bool'>

# print(set_col)    # {'Abdullah', 'Dalal, mashaeal', 'Nasser'}
# print(tuple_col)  # (11, 22, 33, 44, 55, 66)
# print(dict_col)   # {'name': 'Abdullah', 'age': 22}
# print(list_col)   # [33, 44]

# print(type(set_col))    # <class 'set'>
# print(type(tuple_col))  # <class 'tuple'>
# print(type(dict_col))   # <class 'dict'>
# print(type(list_col))   # <class 'list'>


# # Lab 3
# cars = ["GMS", "BMW", "AUDI", "MERCEDES", "TOYOTA", "PORSCHE"]
# print(cars[3])
# print(cars[-1])
# print(cars[-1::-1])  # reverse
# print(cars[-1::])    # last element only


# # Lab 4
# tasks = ["Read email", "Open ticket"]

# tasks[0] = "Login"
# tasks.append("Get Coffee")
# tasks.insert(0, "Get breakfast")
# tasks.pop(3)  # remove the element at index 3 = "Get Coffee"

# print(tasks)


# # Lab 5
# nums = [11, 22, 33, 44, 55, 66]

# print(sum(nums))
# print(min(nums))
# print(max(nums))
# print(len(nums))
# print(math.sqrt(max(nums)))
# print(math.__doc__)
# print(nums)
# print(nums.pop(2))
# print(sorted(nums, reverse=True)) #from max to min


# Lab 6
skills = {"Python", "Django", "Flask", "FastAPI", "Java"}
skills.add("CSS")
skills.add("HTML")
skills.discard("Java")  #.discard if its not found it will not throw an error

print(skills)



