base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (power): "))

result = 1

for i in range(exponent):
    result *= base

print(f"{base} to the power of {exponent} is {result}")