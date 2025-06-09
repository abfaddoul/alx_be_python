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
        print("Commands: deposit, withdraw, display")
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
            print("Invalid command.")
            sys.exit(1)
    
    # Process commands
    if command == "deposit":
        if amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount}")
        else:
            print("Invalid command.")
    
    elif command == "withdraw":
        if amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid command.")
    
    elif command == "display":
        account.display_balance()
    
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()