# 1. Start with x = 0 and apply assignment operators step by step
x = 0
print("Initial x:", x)

x += 10
print("After x += 10:", x)

x -= 3
print("After x -= 3:", x)

x *= 2
print("After x *= 2:", x)

x /= 4
print("After x /= 4:", x)

x %= 3
print("After x %= 3:", x)

print("\n")  # Just a space between tasks


# 3. Simple savings balance calculator: add interest using *=
balance = 1000  # Starting with $1000
interest_rate = 0.05  # 5% interest
years = 3
print("Initial balance:", balance)
for y in range(1, years+1):
    balance *= (1 + interest_rate)
    print(f"After year {y}, balance: {balance:.2f}")

print("\n")

