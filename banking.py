from accounts import BankAccount

def balance():
    total = 0
    for i in range(len(accounts)):
        print("Name:", accounts[i].name , "\tNumbers:", accounts[i].number,
                "\tBalance: ", accounts[i].balance)
        total = total + accounts[i].balance
    print("\t\t\t\t\tTotal: ", total)

def choice():
    choice = input("Enter your transaction selection\n\t(W) Withdrawal\n\t(D) Deposit\n\t(I) Interest\n\t(B) Balance\n\t(X) eXit: ").upper()
    return choice

accounts = []

bank = BankAccount('Everyday','007',2000)
accounts.append(bank)

mychoice = choice()

while mychoice != 'X':
    if mychoice == 'W':
        print("Enter the amount")
        amount = int(input())
        accounts[0].withdraw(amount)
        balance()
        mychoice = choice()
    elif mychoice == 'D':
        print("Enter the amount")
        amount = int(input())
        accounts[0].deposit(amount)
        balance()
        mychoice = choice()
    elif mychoice == 'I':
        accounts[0].add_interest()
        balance()
        mychoice = choice()
    elif mychoice == 'B':
        balance()
        mychoice = choice()
    else:
        mychoice = choice()


