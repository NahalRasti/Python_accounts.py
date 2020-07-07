from accounts import BankAccount
def balance():
    total = 0
    for i in range(len(accounts)):
        print("Name:", accounts[i].name , "\tNumbers:", accounts[i].number,
                "\tBalance: ", accounts[i].balance)
        total = total + accounts[i].balance
    print("\t\t\t\t\tTotal: ", total)

accounts = []
bank = BankAccount('Everyday','007',2000)
accounts.append(bank)
bank = BankAccount('Cheque A/C','008',3000)
accounts.append(bank)
bank = BankAccount('Term Deposit','009',20000)
accounts.append(bank)
balance()

print("\nDoing some transactions...\n")
accounts[0].deposit(100)
accounts[1].withdraw(500)
accounts[2].add_interest()
balance()
