# 15 characters in 1m
student_name = input("Student name: ")
score = int(input("Score: "))

if score >= 90:

    grade = "A"

elif score >= 80:
    grade = "B"

elif score >= 70:
    grade = "C"

else:
    grade = "Needs improvement"

print("Student:" , student_name)
print("Score:" , score)
print("Grade:" , grade)


# 25 characters in 1m

items = ["Coffee", "Sandwitch","Juice"]
prices = [12, 18, 9]

total = 0
for price in prices:
    total += price

vat = total * 0.15
final_total = total + vat

print("Item:")

for item in items:
    print("-" + item)

print("Total:" , total)
print("VAT:" , vat)
print("Final:" , final_total)
