#  1. Sum of odd numbers from 1 to 10

sum_odd = 0
for i in range(1, 11):
    if i % 2 != 0:
        sum_odd += i
print("Sum of odd numbers:", sum_odd)

# 2. Sum of even numbers from 1 to 10

sum_even = 0
for i in range(1, 11):
    if i % 2 == 0:
        sum_even += i
print("Sum of even numbers:", sum_even)

# 3. Sum of numbers from 1 to 10

total = 0
for i in range(1, 11):
    total += i
print("Sum from 1 to 10:", total)

# 4.Find the Greatest of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greatest is:", a)
elif b > a:
    print("Greatest is:", b)
else:
    print("Both are equal")

# 5. Find the Greatest of Three Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest is:", a)
elif b >= a and b >= c:
    print("Greatest is:", b)
else:
    print("Greatest is:", c)

# 6. Print Prime Numbers from 1 to 10

for num in range(1, 11):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# 7. Find if a Year is a Leap Year

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
