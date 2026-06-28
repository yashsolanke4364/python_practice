secret = int(input("enter the secret number: "))
for i in range(1, 4):
    guess = int(input("enter the guess number: "))
    if secret == guess:
        print("the guess is correct")
        break
    else:
        print("the guess is incorrect")
else:
    print("no more guesses")

