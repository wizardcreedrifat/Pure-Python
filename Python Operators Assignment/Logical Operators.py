# 1. Check if a number is positive and even
num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number is NOT both positive and even.")

# 2. Check if a person is eligible to vote (age >= 18) and is a citizen
age = int(input("Enter age: "))
is_citizen = input("Are you a citizen? (yes/no): ").lower() == 'yes'
if age >= 18 and is_citizen:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

# 3. Check if a number is less than 0 or greater than 100
num = int(input("Enter another number: "))
if num < 0 or num > 100:
    print("The number is less than 0 or greater than 100.")
else:
    print("The number is between 0 and 100 (inclusive).")

# 4. Check if a student passed (marks >= 40) and did not cheat
marks = int(input("Enter marks: "))
cheated = input("Did the student cheat? (yes/no): ").lower() == 'yes'
if marks >= 40 and not cheated:
    print("Student passed and did not cheat.")
else:
    print("Student did not pass fairly.")

# 5. Use `not` to reverse a boolean condition
x = True
print("Original:", x)
print("Reversed using not:", not x)
