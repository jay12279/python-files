class BankAccount:
    def __init__(self, account_holder, balance=0): #sets up the account holder and starting balance 
        self.account_holder = account_holder
        self.balance = balance

                # method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

                        # method to withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

                            # method to check balance
    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ₹{self.balance}")

                                      # creating an account with initial balance
acc1 = BankAccount("Tim", 5000)

acc1.display_balance()
acc1.deposit(2000)
acc1.withdraw(1500)
acc1.withdraw(7000)


