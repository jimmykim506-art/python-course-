try:
    number=int(input("Enter A Number:"))
    print("The Number entered is", number)
except valueError as ex: 
    print("Expection:",ex)