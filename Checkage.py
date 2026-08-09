age = int(input("Enter your age: "))

if age >= 10:
    if age <= 20:
        print("You are allowed in the class. Your age is between 10 and 20 years.")
    else:
        print("You are not allowed. Your age is greater than 20 years.")
else:
    print("You are not allowed. Your age is less than 10 years.")