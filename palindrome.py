def palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return original == reverse

num = int(input("Enter a number: "))

if palindrome(num):
    print("Palindrome")
else:
    print("Not a Palindrome")
    