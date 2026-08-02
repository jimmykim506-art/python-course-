a=int(input("enter a number"))
if (a<50):
    amount=a*2.60
    surcharge=25
elif(a<=100):
    amount=130+((a-50)*3.25)
    surchage=35
elif(a<=200):
    amount = 130+162.50+((a-100)*5.26)
    surcharge=45
else:
    amount= 130+162.50+526+((a-200 )*8.45)
    surcharge=75
total=amount+surcharge

print("\nElectricity Bill=%.2f"%total)
