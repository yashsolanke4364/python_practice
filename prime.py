def prime_check(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False
num=int(input("enter a number:"))
print(prime_check(num))