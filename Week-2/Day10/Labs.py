# Lab 1
for attemept in range(3):
    print(f"Attempt {attemept + 1}")
print("Completed")


# Lab 2
for num in range(2, 11, 2):
    print(num)

# Lab 3
for sec in range(10, 0, -1):
    print(f"T-:{sec}")

# Lab4
course = "Python"

for letter in course:
    print(letter)


# Lab 5
student = ["Ammar", "Hassan", "Ali"]

for student in student:
    print("Progressing student:", student)

# Lab 6
for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
    print("---")

# Lab 7
numbers = [1, 2, 3, 4, 5]
even_counter = 0

for num in numbers:
    if num % 2 == 0:
        even_counter += 1
print(f"There are {even_counter} even numbers in the list")


# Lab 8
prices = [23, 30, 55, 115]
total = 0

for price in prices:
    total += price
# 2f means 2 decimal places after the point
print(f"Total: {total} VAT : {total * 0.15:.2f}")

# Lab 9
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
print("Done")

# Lab 10
message = "Please enter your age: "
age_text = input(message).strip()

while not age_text.isdigit():
    print("Invalid input. Please enter a number.")
    # We put it inside the while loop, Becuse we want to ask the user again if there isnt it will be infinite
    age_text = input(message).strip()

age = int(age_text)
print(f"You are {age} years old.")

# Lab 11
password = "" #This can be deleted and it will still work
password = input("Please enter your password")

while password != "python123":
    password = input()
    password = input("Incorrect Password, try again")

print("Password is correct")


# Lab 12
for score in [80, 55, 45, 90]:
    if score < 50:
        pass
    print(f"1 passed  {score}") #print the score

for record in [80, 55, 45, 90]:
    if record < 50:
        print(f"2 passed {record}")     
        continue
    
for bedscore in [80, 55, 45, 90]:
    if bedscore < 50:
        break
    print(f"We saw: {bedscore}")

# Lab 13
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row} X {col}) = {row * col}")

