import task_operations

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            task_operations.add_task(task)

        elif choice == "2":
            task_operations.view_tasks()
            index = input("Enter task number to remove: ")
            task_operations.remove_task(index)

        elif choice == "3":
            task_operations.view_tasks()
            index = input("Enter task number to update: ")
            new_task = input("Enter new task: ")
            task_operations.update_task(index, new_task)

        elif choice == "4":
            task_operations.view_tasks()

        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main()
