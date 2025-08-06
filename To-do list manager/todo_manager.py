tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = input("Enter a task to add: ")
    tasks.append(task)
    save_tasks()
    print("Task added.")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks()
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    global tasks
    tasks = load_tasks()
    while True:
        print("Hi, Welcome to To_do_list Manager!")
        print("\n--- To_do_list Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("User, please choose an option (1-4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Thanks for using To_do_list Manager. Goodbye!")
            break
        else:
            print("Sorry, You Entered invalid choice. Please try again.s")

main()
