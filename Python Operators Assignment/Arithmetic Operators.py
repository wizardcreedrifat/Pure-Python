# 1. Calculate the area and perimeter of a rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

# 2. Convert temperature from Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

# 3. Find the remainder of 25 divided by
divisor = int(input("Enter a number to divide 25 by: "))
remainder = 25 % divisor
print(f"The remainder of 25 divided by {divisor} is: {remainder}")

# 4. Compute the result of 2³ × 5 + 0 / 2 (Following operator precedence)
result = 2**3 * 5 + 0 / 2
print(f"Result of 2^3 × 5 + 0 / 2: {result}")

# 5. Calculate the average of 5 numbers
numbers = []
for i in range(1, 6):
    num = float(input(f"Enter number {i}: "))
    numbers.append(num)
average = sum(numbers) / 5
print(f"Average of the 5 numbers: {average}")
