print("Welcome to the ATM")
initial_balance=5000
print(f"Your initial balance is: ${initial_balance}")
while initial_balance>0:
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice=int(input("enter your choice :"))
    if choice==1:
        print("thye current balance is :",initial_balance)
    elif choice==2:
        deposite=int(input("enter the amount to deposite:"))
        initial_balance=initial_balance+deposite
        print("the current balance is :", initial_balance)
    elif choice==3:
        withdraw=int(input('enter the amount to withdraw:')) 
        if withdraw <= initial_balance:
            initial_balance = initial_balance - withdraw
            print("the current balance is :", initial_balance)
        else:
            print("Insufficient funds")
    elif choice==4:
        print("Thank you for using the ATM. Goodbye!")
        break       