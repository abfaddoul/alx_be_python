# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # الرصيد الأولي

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_input = sys.argv[1]
    if ':' in command_input:
        command, param = command_input.split(':', 1)
        try:
            amount = float(param)
        except ValueError:
            print("Amount must be a number.")
            return
    else:
        command = command_input
        amount = None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
