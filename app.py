from atm import Atm
from sys import exit
import time

time_delay = 1

atm = Atm(150, 250, 10000)  #initiates the class( $20 notes, $50 notes, User balances)
print('\n\t\t\tWelcome to BANK ATM')


def Menu():
    time.sleep(time_delay)
    print('=' * 100)

    option = int(input(
        """
            OPTIONS:

            [ 1 ] Withdraw Funds
            [ 2 ] Deposit Funds
            [ 3 ] Total Account Balance
            [ 4 ] Total Amount of ATM
            [ 5 ] Exit
            \n"""))

    if option == 1:
        user = int(input('Enter the amount of money: '))
        while atm.Check(user) is False:
            print('The amount is not available')
            option = input('Re-enter the amount, press <N>, return to main menu, press <Q>: ').lower()
            if option == 'n':
                user = int(input('Enter the amount of money: '))
            if option == 'q':
                return None
        while atm.Cash_Analysis(user) is False:
            print('the amount is not available')
            option = input('Re-enter the amount, press <N>, return to main menu, press <Q>: ').lower()
            if option == 'n':
                user = int(input('Enter the amount of money: '))
            if option == 'q':
                return None
        total_withdraw = atm.Withdraw_Funds()
        print('Your total amount to your account is: ${}'.format(total_withdraw))

    if option == 2:
        user = int(input('Enter the amount of money: '))
        fifty_user = int(input('Enter the $50 notes number: '))
        twenty_user = int(input('Enter the $20 notes number: '))
        while atm.Check_Deposit(fifty_user, twenty_user, user) is False:
            print('Wrong Amount!')
            option = input('Re-enter the amount, press <N>, return to main menu, press <Q>: ').lower()
            if option == 'n':
                user = int(input('Enter the amount of money: '))
                fifty_user = int(input('Enter the $50 notes number: '))
                twenty_user = int(input('Enter the $20 notes number: '))
            if option == 'q':
                return None
        total_deposit = atm.Deposit_Funds(fifty_user, twenty_user)
        print('Your total amount to your account is: ${}'.format(total_deposit))


    if option == 3:
        print('Your total amount to your account is: ${}'.format(atm.Total_Balances()))

    if option == 4:
        print(atm.Total_Amount_Atm())

    if option == 5:
        print('\t\tThank you for using BANK ATM!')
        exit()

while True:
    Menu()