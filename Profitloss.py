actual_cost=float(input("Please Enter The Actual Price Amount:"))
sale_amount=float(input("Please Enter The Sale Price Amount:"))
if(sale_amount>actual_cost):
    amount=sale_amount-actual_cost
    print("toatal profit={0}".format(amount))
else:
    print("no profit!!")