from Account import Account

account = Account("John Doe", 1000)
print(account._owner)  # This will print "John Doe"
#print(account.__balance)  # This will raise an AttributeError

account.deposit(500)
account.withdraw(200)
print(f"Balance: {account.get_balance()}")
print(f"Owner: {account.get_owner()}")