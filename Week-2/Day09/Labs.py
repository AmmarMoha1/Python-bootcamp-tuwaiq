# Lab 1
age = 20
if 18 <= age <= 60:
    print("welcome")
print("Code Complete")


# Lab 2
tempreture = 31
if tempreture >= 35:
    print("its hot outside")
else:
    print("its cool")

# Lab 3
score = 84
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# Lab 4
is_active = True
is_verified = True
role = "editor"
is_blocked = False

if is_active and is_verified:
    print("Access is ready")

if role == "admin" or role == "editor":
    print("User can edit")

if not is_blocked:
    print("User is not blocked")

# Lab 5
account_active = True
has_permission = False

if account_active:
    if has_permission:
        print("Access granted")
    else:
        print("Access denied")

else:
    print("Account not active")

# Lab 6
name = "Ammar"
cart = []
balance = 990

if name:
    print("Name has a value")
if not cart:
    print("Your cart is empty, please shop")
print(bool(balance))  # True

# Lab 7
name = input("Please enter your name: ").strip()

if not name:
    print("Please enter a name")
elif not name.replace(" ", "").isalpha():
    print("Name must contain only letters")
else:
    print(f"Hello {name}")


# Lab 8
age_text = input("Enter your age: ").strip()
if age_text.isdigit():
    age = int(age_text)
    print(f"you will be {age + 5} years old in 5 years")
else:
    print("Please enter a number")


#Lab 9
is_score_valid = False

score_text = input("Enter a number between 0 and 100: ").strip()
if score_text.isdigit():
    score_x = int(score_text)
    if 0 <= score_x <= 100:
        print("Valid score")
        is_score_valid = True
    else:
        print("Enter score as a number between 0 and 100")
else:
    print("please enter a number")

# Lab 10
membership = ["Admin", "Editor", "Visitor"]

current_membership = input("Enter your membership: ").strip().lower()

if current_membership.title() in membership:
    print("Your are allowed to view this content")
    print(current_membership)
else:
    print("Please contact admin team")
    print(current_membership)

# Lab 11

commands = input("Please enter a command (start , stop, status): ").strip().lower()

match commands:
    case "start":
        print("Starting the application")
    case "stop":
        print("Stopping the application")
    case "status":
        print("Application is running")
    case _:
        print("Invalid command")

