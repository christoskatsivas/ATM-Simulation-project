
class Atm:
    def __init__(self, twenty_note, fifty_note, user_balances):
        self.twenty_note = twenty_note
        self.fifty_note = fifty_note
        self.fifty_cash = None
        self.twenty_cash = None
        self.user_balances = user_balances


    def Cash_Analysis(self, user_funds):
        ''' Analyzes the banknotes available to give the atm '''
        if (user_funds % 50) == 0:
            self.fifty_cash = user_funds//50
            self.twenty_cash = 0

            if self.fifty_note < self.fifty_cash:
                if (user_funds % 20) == 0:
                    self.twenty_cash = user_funds // 20
                    self.fifty_cash = 0
                    if self.twenty_note >= self.twenty_cash:
                        return True
                else:
                    print('The amount is not available.')
                    return False
            return self.fifty_cash, self.twenty_cash

        if (user_funds % 20) == 0:
            self.fifty_cash = (user_funds//100)*2
            self.twenty_cash = (user_funds%100)//20
            if self.fifty_note < self.fifty_cash:
                self.twenty_cash = user_funds // 20
                self.fifty_cash = 0
                if self.twenty_note < self.twenty_cash:
                    print('The amount is not available.')
                    return False
                return self.twenty_cash, self.fifty_cash

        if ((user_funds % 50) != 0) and ((user_funds % 20) != 0):
            if self.fifty_note >= 1:
                user_funds = user_funds - 50
                self.fifty_cash = (user_funds // 100) * 2
                if self.fifty_note < (self.fifty_cash+1):
                    self.twenty_cash = user_funds // 20
                    self.fifty_cash = 1
                    if self.twenty_note < self.twenty_cash:
                        print('The $20 are not available.')
                        return False
                else:
                    self.twenty_cash = (user_funds % 100) // 20
                    self.fifty_cash = self.fifty_cash + 1
                    if self.twenty_note < self.twenty_cash:
                        return False

                return self.twenty_cash, self.fifty_cash
            else:
                print('The $50 are not available.')
                return False

        return True


    def Check(self, user_funds):
        ''' Checks the user's amount if feasible '''
        total_cash = (self.twenty_note * 20) + (self.fifty_note * 50)
        if self.user_balances < user_funds:
            print('Your account does not have the amount you requested.')
            print('Your total amount to your account is: ${}'.format(self.user_balances))
            return False
        if user_funds == 10 or user_funds == 30:
            return False
        if user_funds > total_cash:
            print('ATM does not have the amount you requested.')
            return False
        if (user_funds%10) != 0:
            return False
        return True


    def Check_Deposit(self,fifty_user, twenty_user, user_funds):
        ''' checks whether the amount of money and amount that the user wants to take
            is correct and have the same price '''
        total = (fifty_user * 50) + (twenty_user * 20)
        if total != user_funds:
            return False
        return True


    def Deposit_Funds(self, fifty_user, twenty_user):
        ''' Deposit procedure at ATM '''
        self.twenty_note = self.twenty_note + twenty_user
        self.fifty_note = self.fifty_note + fifty_user
        print('You have made a deposit: {}->$20 notes and {}->$50 notes.'.format(twenty_user,
                                                                                 fifty_user))
        total_d = (twenty_user*20) + (fifty_user*50)
        self.user_balances = self.user_balances + total_d
        return self.user_balances


    def Withdraw_Funds(self):
        ''' procedure for withdrawing funds '''
        self.twenty_note = self.twenty_note - self.twenty_cash
        self.fifty_note = self.fifty_note - self.fifty_cash
        print('You have been withdrawn: {}->$20 notes and {}->$50 notes.'.format(self.twenty_cash,
                                                                                 self.fifty_cash))
        total_w = (self.twenty_cash*20) + (self.fifty_cash*50)
        self.user_balances = self.user_balances - total_w
        return self.user_balances

    def Total_Balances(self):
        ''' Total amount of user in his / her account '''
        return self.user_balances


    def Total_Amount_Atm(self):
        ''' Total amount of ATM '''
        total = (self.twenty_note * 20) + (self.fifty_note * 50)
        return 'The total amount of the ATM is ${}, has <{}: $50> notes and <{}: $20> notes.'.format(total,
                                                                                               self.fifty_note,
                                                                                               self.twenty_note)

