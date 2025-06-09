def display_menu():
    print("\n" + "="*30)
    print("Shopping List Manager")
    print("="*30)
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("="*30)

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip()
            if item:  # Check if item is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Please enter a valid item name.")
                
        elif choice == '2':
            # Prompt for and remove an item
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
            else:
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from your shopping list.")
                else:
                    print(f"'{item}' is not in your shopping list.")
                    
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print(f"\nYour Shopping List ({len(shopping_list)} items):")
                print("-" * 25)
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                    
        elif choice == '4':
            print("Thank you for using Shopping List Manager!")
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
