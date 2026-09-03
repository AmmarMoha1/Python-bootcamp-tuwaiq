# list comperhension , odd numbers
numbers = [1, 2, 3, 4, 5]  # assign statment

squares = [  # squares comperhension
    number ** 2  # expression
    for number in numbers  # clause
    if number % 2 == 1  # Filter
]

print(squares)  # [1, 9, 25]


prices = [10, 25, 40]  # assign

prices_with_vat = [
    round(price * 1.15, 2)  # expression
    for price in prices  # clause
]

print(prices_with_vat)  # [11.5, 28.75, 46.0]


scores = [42, 67, 91, 58, 75]

passing_scores = [
    score  # expression
    for score in scores  # clause
    if score >= 60  # Filter
]

print(passing_scores)  # [67, 91, 75]

raw_names = [" sara ", "", "OMAR", " lina"]

cleann_names = [
    name.strip().title()
    for name in raw_names
    if name.strip()  # First Filter and if no name it will be false
]
print(cleann_names)

numbers = [1, 2]
letters = ["A", "B"]

# multiple list comprehension
pairs = [
    (number, letter)  # expression
    for number in numbers  # clause
    for letter in letters  # clause
]
print(pairs)


scores = [42, 67, 91]

# condition expression
labels = [
    "pass" if score >= 60 else "retry"
    for score in scores  # clause
]

print(labels)

emails = [
    "SARA@EXAMPLE.com",
    "omar@example.com",
    "lina@school.sa"
]

domains = {  # set no duplicates
    email.split("@")[1].lower()  # expression
    for email in emails  # clause
}

print(domains)  # {'example.com', 'school.sa'}


numbers = range(1, 6)

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} dictionary comprehension
