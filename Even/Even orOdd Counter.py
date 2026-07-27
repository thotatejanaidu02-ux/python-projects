n = int(input("Enter a number (N): "))

even_count = 0
odd_count = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even numbers (1 to {n}): {even_count}")
print(f"Odd numbers (1 to {n}): {odd_count}")
