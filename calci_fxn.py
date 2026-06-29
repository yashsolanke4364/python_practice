print("welcome to the calcultor!")
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a/b
while a>0 and b>0:
     print("1. addition")
     print("2. subtraction")
     print("3. multiplication")
     print("4. division")
     print("5. Exit")
     choice=int(input("enter your choice :",))
     if choice==1:
        print("the addition is :",add(a,b))
     elif choice==2:
        print("the subtraction is :",subtract(a,b))
     elif choice==3:
        print("the multiplication is :",multiply(a,b))
     elif choice==4:
        print("the division is :",divide(a,b))
     elif choice==5:
        print("Thank you for using the calculator!")
        break       
