class BankAccount:
    def __init__(self, acct_no="", int_rate=0.02, balance=0):
        self.acct_no = acct_no
        self.balance = balance
        self.interest_rate = int_rate
    # def __str__(self):
    #     output_str1 = f"Account: {self.name}; Account balance: {self.balance}; Interest rate: {self.interest_rate}"
    #     return output_str1
    def deposit(self, amount):
        self.balance += amount
        return self

    # Add a withdraw method to the BankAccount class
    # decreases the account balance by the given amount if
    #  there are sufficient funds; if there is not enough money,
    #  print a message "Insufficient funds: Charging a $5 fee"
    # and deduct $5
    def withdraw(self, amount):
        self.balance -= amount
        if amount > self.balance:
            print(f"Account {self.acct_no} doesn't have sufficient funds for this withdrawal: Charging a $5 fee")
            self.balance -= 5    
        return self
    
    # Add a display_account_info method to the BankAccount class
    # print to the console: eg. "Balance: $100"
    def display_account_info(self):
        output_str1 = f"Account: {self.acct_no}; Balance: ${self.balance}; Interest rate: {self.interest_rate}"
        print(output_str1)
        return self


# Update the User class __init__ method
class User:		# declare a class and give it name User
    def __init__(self, name, email): 
        self.name = name
        self.email = email
        # self.account = BankAccount(name = "Account", int_rate = 0.02, balance=0)
        self.account = {}
    def __str__(self):
        output_str = f"name: {self.name}; Email: {self.email};"
        #  output_str = f"name: {self.name}; Email: {self.email}; Bank account interest rate: {self.account.interest_rate}; Account balance: {self.account.balance}"
        return output_str
    
    def open_new_account(self, acct_no="", interest_rate=0.02, balance=0):
        self.account[acct_no] = BankAccount(acct_no= acct_no, int_rate=interest_rate, balance=balance)
        print(f"Account acct_no {acct_no} for {self.name} has been opened")
        return self

    # Update the User class make_deposit method
    def make_deposit(self, acct_no, amount):
        self.account[acct_no].deposit(amount)
        print(f"{self.name} has deposited ${amount}")
        return self    

    # Update the User class make_withdrawal method
    def make_withdrawal(self, acct_no, amount):
        self.account[acct_no].withdraw(amount)
        print(f"{self.name} has withdrawn ${amount}")
        return self

    # Update the User class display_user_balance method
    def display_user_balance(self, acct_no):
        print(f"User: {self.name}; Balance: ${self.account[acct_no].balance}")
        return self

    # SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to 
    # specify which account they are withdrawing or depositing to


# Create 3 instances of the User class
abby = User("Abby", "abby@gmail.com")
max = User("Max", "m@gmail.com")
cassidy = User("Cassidy", "c@gmail.com")

abby.open_new_account(1, balance=100).open_new_account(2)
max.open_new_account(1)
cassidy.open_new_account(1)




# Have the first user make 3 deposits and 1 withdrawal and 
# then display their balance
abby.make_deposit(1, 50).make_deposit(1, 100).make_deposit(1, 20)
abby.display_user_balance(1)

# # Have the second user make 2 deposits and 2 withdrawals 
# # and then display their balance
max.make_deposit(1, 100).make_deposit(1, 50).make_withdrawal(1, 40).make_withdrawal(1, 20)
max.display_user_balance(1)


# # Have the third user make 1 deposits and 3 withdrawals 
# # and then display their balance
cassidy.make_deposit(1, 300).make_withdrawal(1, 50).make_withdrawal(1, 40).make_withdrawal(1, 60)
cassidy.display_user_balance(1)

