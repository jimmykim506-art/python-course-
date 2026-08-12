num=int(input("Enter A Number"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==num:
    print("Its a Armstrong Number")
else:
    print("Not a Armstrong Number")
