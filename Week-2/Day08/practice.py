
print("Hello There, insert two sentences and two numbers")

sentence1 = input("Enter three names: ")
sentence2 = input("Enter second sentence to slicing: ")

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))


calculate = number1 + number2
equal = number1 == number2
equal2 = number1 is number2
floor_division = number1 // number2


# Split the sentence
x = sentence1.split()
print("After split:")
print(x)


# Join the list
joined_sentence = " | ".join(x)
print("\nAfter join:")
print(joined_sentence)


# String slicing
print("\nSentence slicing:")
print(sentence2[0:5])


print("\nNumbers:")
print("First number:", number1)
print("Second number:", number2)
print("Sum:", calculate)
print("numbers are equal ? :", equal)
print("numbers are identical ? :", equal2)
print("Floor division:", floor_division)


# List operations
numbers = [1, 2, 3]
print("Numbers before adding:", numbers)
numbers.append(4)

print("Numbers after adding:", numbers)

numbers.remove(3)
print("Numbers after removing 3:", numbers)


# Calculate the number of full boxes and remaining items
total_items = 17
box_capacity = 5

full_boxes = total_items // box_capacity
remaining_items = total_items % box_capacity


print("Full boxes:", full_boxes)
print("Remaining items:", remaining_items)
