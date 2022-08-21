from tkinter import W


print("Welcome To SAM CODEHUB Bank ATM")
restart = ('Y')
chances = 3
balance = 12.18
while chances >= 0:
    pin = int(input("Please Enter Your 4 Digit Pin: "))
    if pin == (0000):
        print("Pin Successfully Entered\n")
        while restart not in('n','NO','no','N'):
            print("Please Press 1 For Your Balance\n")
            print("Please Press 2 To Make A Withdrawl\n")
            print("Please Press 3 To Pay In\n")
            print("Please Press 4 To Return Your Card\n")
            option = int(input('What Would You Like To Choose? '))
            if option == 1:
                print('Your Balance Is $',balance,'\n')
                restart = input('would you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('Y')
                withdrawl = float(input('How Much Would You Like To Withdraw? \n$10/$20/$30/$50/$100 For Other Enter 1: '))
                if withdrawl in [10, 20, 30, 50, 100]:
                    balance = balance - withdrawl
                    print('\nYour Balance Now Is $',balance)   
                    restart = input('Would You Like To Go Back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl != [10, 20, 30, 50, 100]:
                    print('Invalid Amount, please enter a new amount\n')
                    restart =('Y')
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Your Desired Amount:'))
                elif option == 3:
                    Pay_in = float(input('HOW MUCH WOULD YOU LIKE TO PAY IN: '))
                    balance = balance + Pay_in
                    print('\nYour Balance Now Is $',balance)
                    restart = input('Would You Like To Go Back? ')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif option == 4:
                    print('Please Wait While Your Card Is Returned...\n')
                    print('Thank You For Using Our Service')
                    break
                else:
                    print('Please Enter A Correct Number..\n')
                    restart = 'Y'
            elif pin != ('0000'):
                print('INCORRECT PASSWORD!!!')
                chances = chances - 1 
                if chances == 0:
                    print('\nNO MORE TRIES')
                    break
                    