max_num = int(input("Enter a maximum number: "))
total = 0
count_even = 0
for num in range(1, max_num+1):
    num_even = num % 2 == 0
    if num_even:
        total += num
        print("Even number:", num)
        count_even += 1
    else:
        print("Odd number:", num)
print("There are", count_even, "even numbers between 1 and", max_num)
print("The sum of all even numbers between 1 and", max_num, "is", total)
