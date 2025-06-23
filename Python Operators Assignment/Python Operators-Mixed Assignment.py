# Input the student's details
name = input("Enter the student's name:  ")
marks = []

for i in range(1, 4):
    mark = int(input(f"Enter marks for subject {i} (out of 100): "))
    marks.append(mark)

# Calculate total, average, and percentage
total = sum(marks)
average = total / 3
percentage = (total / 300) * 100

# Assign grade
if average >= 80:
    grade = 'A'
elif average >= 70:
    grade = 'B'
elif average >= 50:
    grade = 'C'
else:
    grade = 'F'

# Check if passed (all subjects >= 40)
passed = all(mark >= 40 for mark in marks)

# Check scholarship eligibility (average >= 85 and no subject below 80)
scholarship = average >= 85 and all(mark >= 80 for mark in marks)

# Print initial report
print("\n--- Student Report ---")
print(f"Name: {name}")
print(f"Marks: {marks}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Passed: {'Yes' if passed else 'No'}")
print(f"Scholarship Eligible: {'Yes' if scholarship else 'No'}")

# Add a bonus of 5 marks to each subject using '+='
for i in range(3):
    marks[i] += 5
    # Maximum mark per subject is 100
    if marks[i] > 100:
        marks[i] = 100

# Recalculate total and average after bonus
total_bonus = sum(marks)
average_bonus = total_bonus / 3

# Print updated report
print("\n--- Updated Report After Bonus ---")
print(f"Marks after bonus: {marks}")
print(f"Total after bonus: {total_bonus}")
print(f"Average after bonus: {average_bonus:.2f}")
