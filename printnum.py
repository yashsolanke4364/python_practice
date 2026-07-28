def print_1to100():
 for i in range(0,101):
    print(i)
def print_even():
  for i in range(0,101,2):
    print(f" {i}")
def odd_num():
  for i in range(0,101):
   if i%2!=0 :
    print(i)  
def table_of_num(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")  
def sum_of_num(n):
  total = 0
  for i in range(0,n):
    total += i
  print(total)

def factorial(n):
  if n < 0:
    print("the factorial of the negative number is not possible")
    return None
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result
def reverse_num(num2):
    reversed_num = 0
    while num2 > 0:
        digit = num2 % 10
        reversed_num = reversed_num * 10 + digit
        num2 //= 10
    return reversed_num


print_1to100()
print_even()
odd_num()
num=int(input("Enter the number to print its table: "))
table_of_num(num)
n=int(input("enter the value of n:"))
sum_of_num(n)
x=int(input("enter the number to find factorial:"))
print("the factorial of the number is :", factorial(x))
num2=int(input("enter the value of num:"))
print("the reversed number is :", reverse_num(num2))

