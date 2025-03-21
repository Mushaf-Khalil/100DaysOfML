import os

TASKS_FILE = "tasks.txt"

def ensure_file_exists():
    """Ensure the tasks file exists."""
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as file:
            pass  # Create an empty file

def read_tasks():
    """Read tasks from the file and return as a list."""
    ensure_file_exists()
    with open(TASKS_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def write_tasks(tasks):
    """Write a list of tasks back to the file."""
    with open(TASKS_FILE, "w") as file:
        file.writelines("\n".join(tasks) + "\n")
