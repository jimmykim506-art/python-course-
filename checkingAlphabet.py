ch = input("Enter a character: ")

# Check if the character is an alphabet using comparison operators
if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
    print(ch, "is an alphabet.")
else:
    print(ch, "is not an alphabet.")
