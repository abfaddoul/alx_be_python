import sys
from bank_account import BankAccount

def main():
    """
    Main function to handle command line banking operations.
    
    This script creates a BankAccount instance and processes command line
    arguments to perform banking operations like deposit, withdraw, and display.
    """
    # Create account with starting balance of $100
    account = BankAccount(100)
    
    # Check if command line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands:")
        print("  deposit:<amount>  - Deposit money into account")
        print("  withdraw:<amount> - Withdraw money from account")
        print("  display          - Show current balance")
        print("Examples:")
        print("  python main-0.py deposit:50")
        print("  python main-0.py withdraw:20")
        print("  python main-0.py display")
        sys.exit(1)
    
    # Parse command and parameters
    command_parts = sys.argv[1].split(':')
    command = command_parts[0].lower()
    
    # Extract amount if provided
    amount = None
    if len(command_parts) > 1:
        try:
            amount = float(command_parts[1])
        except ValueError:
            print("Error: Amount must be a valid number.")
            sys.exit(1)
    
    # Process commands
    if command == "deposit":
        if amount is not None and amount > 0:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Error: Please provide a valid positive amount for deposit.")
    
    elif command == "withdraw":
        if amount is not None and amount > 0:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Error: Please provide a valid positive amount for withdrawal.")
    
    elif command == "display":
        account.display_balance()
    
    else:
        print(f"Invalid command: {command}")
        print("Valid commands: deposit, withdraw, display")

if __name__ == "__main__":
    main()