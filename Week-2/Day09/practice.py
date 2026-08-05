print("Welcome to the Lab Management System!")

student_name = input("Enter your name: ")

if student_name.isalpha():
    print(f"Hello, {student_name}!")

    score = input("Enter your score (0-100): ")

    if score.isdigit():
        score = int(score)

        if 0 <= score <= 100:

            if score >= 90:
                print("Congratulations! You have an A grade.")
            elif score >= 80:
                print("Great job! You have a B grade.")
            elif score >= 70:
                print("Good effort! You have a C grade.")
            elif score >= 60:
                print("You have a D grade.")
            else:
                print("You have an F grade.")

            print(f"Your score is {score}.")

            print("Choose your course from the following options:")
            print("1. Math")
            print("2. Science")
            print("3. History")

            choice = input("Enter your choice (1-3): ")

            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= 3:
                    if choice == 1:
                        course = "Math"
                    elif choice == 2:
                        course = "Science"
                    else:
                        course = "History"

                    print(f"You have chosen the {course} course.")
                else:
                    print("Invalid choice. Enter a number between 1 and 3.")
            else:
                print("Invalid choice. Please enter numbers only.")

        else:
            print("Invalid score. Enter a number between 0 and 100.")

    else:
        print("Invalid score. Please enter numbers only.")

else:
    print("Invalid name. Please enter letters only.")
