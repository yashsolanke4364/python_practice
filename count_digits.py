num=int(input("enter a number:"))
count=0
while num>0:
    num=num//10
    count=count+1
print("the number of digits in the number is:",count)