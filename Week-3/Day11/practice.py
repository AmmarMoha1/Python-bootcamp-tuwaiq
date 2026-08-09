def calculate_grade():
    name = input("Enter your name: ")
    score = input("Enter your score: ")

    if name == "" or name.isdecimal():

        print("Please enter your name")
        return

    if not score.isdigit():
        print("Error: Score must be a number")
        return
    
    score = int(score)

    if score < 0 or score > 100:
        print("Error: Score must be between 0 and 100")
        return

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Name: {name}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")

calculate_grade()
    
    