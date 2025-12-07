import sys
from bank_account import BankAccount

# The main function handles command-line interaction
def main():
    # Create an account with an initial balance of 0
    account = BankAccount(0)

    # Ensure the user provides a command when running the script
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the command (e.g., "deposit:50" → command="deposit", amount="50")
    command, *params = sys.argv[1].split(':')

    # Convert amount to float if it exists (display command has no amount)
    amount = float(params[0]) if params else None

    # Handle deposit command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")

    # Handle withdraw command
    elif command == "withdraw" and amount is not None:
        # withdraw() returns True if money was successfully withdrawn
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    # Handle display command – shows current balance
    elif command == "display":
        account.display_balance()

    # If the command is not valid
    else:
        print("Invalid command.")

# Ensures main() runs only when this script is executed directly
if __name__ == "__main__":
    main()
