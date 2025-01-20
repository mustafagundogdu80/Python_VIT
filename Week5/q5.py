"""
Question5: Create a "Customer" class and an "Account" class. Let the "Account" class inherit from the "Customer" class and represent a customer's bank account information.

Customer Class Features:
    "name" (customer name)
    "surname" (customer surname)
    "tc_identification" (customer TR ID number)
    "phone" (customer phone number)
Account Class Properties:
    "customer" (a Customer object)
    "account_number" (account number)
    "balance" (account balance)
Customer Class Method:
    "display_information()": Displays the customer's name, surname, TR ID number and telephone number.
Account Class Methods:
    "deposit(self, amount)": A method that deposits a certain amount of money into the account.
    "money_check(self, amount)": A method that withdraws a certain amount of money from the account. However, if there is not enough balance in the account, the transaction should not occur and a message should be displayed.
    "display_balance()": A method that displays the account balance.
Create these two classes, then create a Customer object and an Account object, add the customer information to the Account object, and perform account operations and view the results.
"""
class Customer:
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"TC Identification: {self.tc_identification}")
        print(f"Phone: {self.phone}")

# class Account:
#     def __init__(self, customer, account_number, balance=0):
#         self.customer = customer
#         self.account_number = account_number
#         self.balance = balance
    
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount} € deposited to the account. New balance: {self.balance} €")

#     def money_check(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"{amount} € withdrawn from the account. New balance: {self.balance} €")
#         else:
#             print("Insufficient balance.")

#     def display_balance(self):
#             print(f"Account balance: {self.balance} €")
class Account(Customer):
    def __init__(self, name, surname, tc_identification, phone, account_number, balance=0):
        super().__init__(name, surname, tc_identification, phone)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} € deposited to the account. New balance: {self.balance} €")    

    def money_check(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} € withdrawn from the account. New balance: {self.balance} €")
        else:
            print("Insufficient balance.")

    def display_balance(self):
            print(f"Account balance: {self.balance} €")

if __name__ == "__main__":
    # customer = Customer("Omer", "Sami", "12345678901", "1234567890")
    # account = Account(customer, "123123123", 1000)
    account = Account("Omer", "Sami", "12345678901", "1234567890", "123123123", 1000)
    print("----------------------------------")
    # account.customer.display_information()
    account.display_information()
    print("----------------------------------")
    account.display_balance()
    print("----------------------------------")
    account.deposit(500)
    print("----------------------------------")
    account.money_check(200)
    print("----------------------------------")
    account.display_balance()
    print("----------------------------------")
    input()