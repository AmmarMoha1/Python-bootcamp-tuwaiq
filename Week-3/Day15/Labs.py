# Lab 1
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for number in numbers:
    squared_numbers.append(number ** 2)

print(squared_numbers)

#comprehension
squared_numbers = [
    number ** 2 
    for number in numbers
]
print(squared_numbers)


# Lab 2
prices = [10, 25, 40]

prices_with_vat = [
    round(price * 1.15, 2)
    for price in prices
]
print(prices_with_vat)


# Lab 3
names = ["SaRa", "ArEeJ", "Mashael", "nasser"]

lower = [
    name.lower()
    for name in names
]

upper = [
    name.upper()
    for name in names
]

titled = [
    name.title()
    for name in names
]

print(lower)
print(upper)
print(titled)


# Lab 4
c_temp = [20, 33, 15, 1]

f_temp = [
    (temp * 1.8) + 32
    for temp in c_temp
    if temp > 0
]

print(f_temp)


# Lab 5
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = []
for row in nested_list:
    for item in row:
        flattened_list.append(item)

print(flattened_list)

#comprehension
comp_flattened_list = [
    colomn
    for row in nested_list
    for colomn in row
]

print(comp_flattened_list)


# Lab 6
scores = [45, 55, 65, 75, 86, 95]
passing_scores = [
    "pass" if score >= 60 else "fail"
    for score in scores
]

print(passing_scores)


# Lab 7
skills = ["PYTHON", "Git", "python", "Javascript", "SQL", "git"]
skills_set = {
    skill.lower()
    for skill in skills
}
print(skills_set)


# Lab 8
list_name = ["Sara", "Dalal", "Nouf", "Taif"]

counted_chars = [
    {
        "name": name,
        "count": len(name)
    }
    for name in list_name
]

print(counted_chars)


# Lab 9 
new_names = ["Mada", "Khadija", "Sara", "Ahmed"]

upp = (
    name.upper()
    for name in new_names

)
print(next(upp)) #MADA
print(next(upp)) #KHADIJA
print("-" * 10) 
for x in upp:    
    print(x)     #SARA, AHMED


