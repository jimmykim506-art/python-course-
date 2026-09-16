try:
    num1, num2= eval(input("Enter two numbers, seperated by a comma:"))
    result=num1/num2
    print("Reslts is", result)
except ZeroDivisionError:
    print(" Division by 0 is Error")
except SyntaxError:
    print("Comma is missing enter number seperated by comma like this 1,2")
except:
    print("Wrong input")
else:
    print("No excpetion")
finally:
    print(" This will exceute no matter what")