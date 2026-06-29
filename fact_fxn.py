def factorial(n):
    if n<0 :
        print("the factorial of the negaative number is not possible")
    elif n==0:
        print("the factorial of 0 is always 1 ")
    else:
        factorial=1
        for i in range (1,n+1):
            factorial=factorial*i
    return factorial
x=int(input("enter the number:"))
print("the factorial of the number is :", factorial(x))

        