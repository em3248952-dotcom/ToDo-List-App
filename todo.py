tasks = []

def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "status": "Not Done"})
    print(f"Task '{title}' added.")

def list_tasks():
    print("\n--- To-Do List ---")
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} [{task['status']}]")

def mark_done():
    list_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to mark done: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["status"] = "Done"
                print("Task updated!")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a number.")

while True:
    print("\n1. Add Task  2. List Tasks  3. Mark Done  4. Exit")
    choice = input("Choose: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
