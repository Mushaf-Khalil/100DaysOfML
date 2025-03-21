from file_handler import read_tasks, write_tasks

def add_task(task):
    """Add a new task to the list."""
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    print("Task added successfully!")

def remove_task(index):
    """Remove a task by index."""
    tasks = read_tasks()
    try:
        index = int(index) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number!")
            return
        del tasks[index]
        write_tasks(tasks)
        print("Task removed successfully!")
    except ValueError:
        print("Please enter a valid number.")

def update_task(index, new_task):
    """Update a task by index."""
    tasks = read_tasks()
    try:
        index = int(index) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number!")
            return
        tasks[index] = new_task
        write_tasks(tasks)
        print("Task updated successfully!")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks():
    """Display all tasks."""
    tasks = read_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
