#simple calculator in python
def add (x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def calculator():
    print("select operation:")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
choice = input("enter choice(1/2/3/4):")
if choice in['1','2','3','4']:
    num1 = float(input("enter first numkber:"))
    num2 = float(input("enter second number"))
    if choice =='1':
        print(f"{num1}+{num2}={add(num1,num2)}")
    elif choice =='2':
        print(f"{num1}-{num2}={subtract(num1,num2)}")
    elif choice =='3':
        print(f"{num1}*{num2}={multiply(num1,num2)}")
    elif choice =='4':
        print(f"{num1}/{num2}={divide(num1,num2)}")
    else:
        print("invalid input!")
        if__name__=="__main__"
        calculator()