medical_cause=input("Do you Have a medical cause (Y/N)").strip().upper()
if medical_cause=="Y":
    print("You are allowed")
else:
        attend=int(input("Enter the attendance of the student"))
        if attend>=75:
              print("Your Are Allowed")
        else:
              print("Your Are not Allowed")
                   