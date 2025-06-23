# 1. Check if two numbers are equal
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a == b:
    print("The two numbers are equal.")
else:
    print("The two numbers are NOT equal.")

# 2. Compare ages of two people and print who is older
age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
if age1 > age2:
    print("Person 1 is older.")
elif age2 > age1:
    print("Person 2 is older.")
else:
    print("Both are of the same age.")

# 3. Program to determine if a year is before or after 2000
year = int(input("Enter a year: "))
if year < 2000:
    print("Year is before 2000.")
elif year > 2000:
    print("Year is after 2000.")
else:
    print("Year is 2000.")

# 4. Take two numbers, check which one is greater
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater.")
elif num2 > num1:
    print(f"{num2} is greater.")
else:
    print("Both numbers are equal.")

# 5. Compare marks of two students to check if both got the same score
marks1 = float(input("Enter marks of student 1: "))
marks2 = float(input("Enter marks of student 2: "))
if marks1 == marks2:
    print("Both students got the same score.")
else:
    print("Students got different scores.")

# 6. Check if a number is not equal to zero before dividing
num = float(input("Enter a number to divide 100 by: "))
if num != 0:
    result = 100 / num
    print(f"100 divided by {num} is {result}")
else:
    print("Cannot divide by zero!")
