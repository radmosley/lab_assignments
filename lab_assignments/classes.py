#requiremnets:
#name
#account number
#account balance
#phone number

# accounts = {
#     00001: {
#         'name: chriss',
# 'phone': 8328584422,
# 'balance': 10
#         }
#     }

NUMBER_OF_ACCOUNTS = 0

class BankAccount:
    def __init__(self, client_name):
        self.account_number = self.assign_account_number()
        self.name = client_name
        self.balance = 0
        self.phone = phone

    def assign_account_number(self):
        global NUMBER_OF_ACCOUNTS
        NUMBER_OF_ACCOUNT += 1
        return NUMBER_OF_ACCOUNTS

    def deposit(self, amount):
        self.bank += amount
        print("thanks {}! Your Balance is now{}.".format(self.name, self.balance))

    def widthdrawl(self, amount):
        if self.balance - amount >= 0:
            self.bank -= amount
            print("thanks {}! Your Balance is now{}.".format(self.name, self.balance))
        else:
            print('I\'m sorry {}, you do not have enough moeny for that.')

class BankAccountPlus(BankAccount):
    def __init__(self,client_name):
        super().__init__(name, phone)

    def widthdrawl(self, amount):
        if self.balance - amount >= 100:
            self.bank -= amount
            print("thanks {}! Your Balance is now{}.".format(self.name, self.balance))
        elif 100 > self.balance - amount:
            print('I\'m sorry {}, you do not have enough moeny for that.')

chris_account = BankAccount('chris')
sheri_account = BankAccount('sheri')

print(sheri_account.name)
print(chris_account.name)