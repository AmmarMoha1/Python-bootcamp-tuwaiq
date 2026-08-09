# Lab 1
def greet():
    print("Welcome")

greet()

# Lab 2
def show_menu():
    print("1- Coffee")
    print("2- Tea")
    print("3- Juice")

show_menu()
print("Outside the call")
show_menu()

# Lab 3
print("Line One")
def gotofunc():
    print("From within the Goto")

print("Where is line 2?")
gotofunc()
print("I'm up here")

# Lab 4 
def greet_student(name):
    print(f"Hello {name}")

greet_student("Ammar")

# Lab 5
def show_booking(destination = "London", nights = "1"):
    if nights.isdigit():
        nights = int(nights)
    print(f"You have booked a trip to {destination} for {nights} nights")

show_booking()
show_booking(5, "Dubai") # 5 not error becuse no validation
show_booking("Doha", 2) # 2 is the default value for night, Error

# Lab 6
def getVAT(total, rate = 0.15):
    """" This Function will calculate the VAT of a total amount with a default value of 15% """
    subtotal = total + (total * rate)
    return subtotal

print(getVAT(100))
print(getVAT(100, 0.05))
print(getVAT.__doc__)
print(getVAT.__name__)
help(getVAT)



