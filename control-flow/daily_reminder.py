# daily_reminder.py

def get_input(prompt, valid_options=None):
    while True:
        user_input = input(prompt).strip().lower()
        if valid_options:
            if user_input in valid_options:
                return user_input
            else:
                print(f"Please enter one of the following: {', '.join(valid_options)}")
        else:
            if user_input:
                return user_input
            else:
                print("Input cannot be empty.")

def main():
    task = get_input("Enter your task: ")
    priority = get_input("Priority (high/medium/low): ", valid_options=["high", "medium", "low"])
    time_bound = get_input("Is it time-bound? (yes/no): ", valid_options=["yes", "no"])

    reminder = ""

    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an unknown priority"

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    print("\nReminder:", reminder)

if __name__ == "__main__":
    main()
