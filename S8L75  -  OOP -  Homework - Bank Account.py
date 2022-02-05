
# Create a bank account class that has two attributes:
# owner
# balance

# and two methods:
# deposit
# withdraw

# Withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals,
# and test to make sure the account can't be overdrawn.

class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, summ):
        self.balance += summ
        print(f"Deposit Accepted. Current state: {self.balance}")

    def withdraw(self, summ):
        if self.balance >= summ:
            self.balance -= summ
            print(f"Current state: {self.balance}")
        else:
            print("Not enough funds to withdraw.")

    def __str__(self):
        return (f"Account owner: {self.owner} \nAccount balance: {self.balance}")


# 1. Instantiate the class
acct1 = BankAccount('Jose',100)

# 2. Print the object
print(acct1)
# Account owner: Jose
# Account balance: 100

# 3. Show the account owner attribute
acct1.owner
# 'Jose'

# 4. Show the account balance attribute
acct1.balance
# 100

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
# Deposit Accepted. Current state: 150

acct1.withdraw(50)
#Current state: 100

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
# Not enough funds to withdraw.

