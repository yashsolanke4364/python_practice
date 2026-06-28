num=int(input("enter a number:"))
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num//=10
print("the reversed number is :",reverse)