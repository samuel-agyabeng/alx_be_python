# Greetings 
print("Welcome to your daily reminder app.")

#Request for task details 
task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low)")
time_bound = input("Is it time-bound? (yes/no): ").lower()

#match case to process outputs 
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a high priority task but does not require immediate attention.")
        else:
            print("You entered the wrong value, try again")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that requires timely attention.")
        elif time_bound == "no":
            print(f"Note: {task} is a medium priority task. Complete it when possible.")
        else:
            print("You entered the wrong value, try again")

    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task but still requires attention today.")
        elif time_bound == "no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print("You entered the wrong value, try again")

    case _:
        print("Invalid priority. Please enter high, medium, or low.")
        