def show_menu():
    print("\n--- TODO LIST MANAGER ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            if not tasks:
                print("\nYour task list is empty!")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")

        elif choice == "2":
            new_task = input("\nEnter the task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Task '{new_task}' added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "3":
            if not tasks:
                print("\nNo tasks to delete!")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                
                try:
                    task_num = int(input("\nEnter task number to delete: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"Task '{removed}' deleted!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
