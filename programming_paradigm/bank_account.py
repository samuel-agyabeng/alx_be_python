# bank_account.py
# This file defines a simple BankAccount class with basic banking operations

class BankAccount:
    """A simple bank account class."""

    def __init__(self, account_balance=0):
        """Initialize the account with a starting balance (default 0)."""
        self.account_balance = account_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Deduct the amount from account balance if funds are sufficient.
        Returns True if withdrawal was successful, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Your account balance is: ${self.account_balance}")
