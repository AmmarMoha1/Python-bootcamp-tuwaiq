
# Lab 1
result = 10 + 5 * 2 - 4 / 2
print(result)

# Lab 2
total_items = 17
box_capacity = 5
full_boxes = total_items // box_capacity
remaining_items = total_items % box_capacity

print("Full boxes:", full_boxes)
print("Remaining items:", remaining_items)

# Lab 3
base_calc = 2 + 3 * 2 ** 2
gcalc = (2 + 3 * 2) * 2 ** 2

print(base_calc)
print(gcalc)

# Lab 4
user_age = 25
has_permission = True

is_eligible = user_age >= 18 and has_permission
print("Is the user eligible?", is_eligible)

# Lab 5
score = 10
score += 5
score *= 5

print("Final score:", score)

# Lab 6
memberships = ["Gold", "Silver", "Bronze"]
current_membership = "Silver"

if current_membership and "Gold" in memberships:
    print("Membership is valid.")
else:
    print("Membership is not valid.")

# Lab 7

sentence = "Python web development"

new_sentence = sentence.find("P")  # Find the index of the word "web"
print(type(new_sentence))
print(new_sentence)

# Lab 8
message = "Python is a programming language"
first_char = message[0]
last_char = message[-1]
print(f"first character: {first_char}, last character: {last_char}")
# slicing
sliced_message = message[:6]
print(sliced_message)

sliced_message1 = message[::6]
print("jump 6: "+sliced_message1)
reveresed_message = message[::-1]
print("Reversed message:"+reveresed_message)

# Lab9
my_email = "    amar@TUWAIQ.com"
cleaned_email = my_email.strip().lower()
message2 = "Development by python"
titled_message = message2.title()
print(f"Your emails: {cleaned_email},and your course is {titled_message}")

# Lab 10
csv_text = "apple, orange , banana, grape"

splitted_text = csv_text.split(",")
print("split text:"+str(splitted_text))

joined_text = " -".join(splitted_text)
print("joined text: "+joined_text)

# Lab 11
# Use a try and except block to handle the error when trying to modify a string (which is immutable in Python).
name = "Amar"
try:
    name[0] = "O"
except TypeError as e:
    print("Error:", e)


x = [5]
y = [5]

if (x is y):
    print("x and y are same value")
else:
    print("x and y are not same value")

print(id(x))
print(id(y))


# Lab 12
message3 = "Python is a programming language"
new_message3 = message3.replace("Python", "Java")
print(new_message3)


# Lab 13
x = 5
y = 10

x, y = y, x
print("After swapping: x =", x, "y =", y)

is_online = None

if (is_online):
    print("True")
elif (is_online != True and is_online != False):
    print("False")
else:
    print("None")
