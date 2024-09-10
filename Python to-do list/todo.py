task_items = []

def show_options():
    print("\n1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Mark task as done")
    print("5. Edit a task")
    print("6. Exit")

def add_task():
    new_task = input("Enter task: ")
    task_items.append({"task": new_task, "done": False})
    print(f"Task '{new_task}' added.")

def remove_task():
    remove_task = input("Enter task to remove: ")
    for t in task_items:
        if t['task'] == remove_task:
            task_items.remove(t)
            print(f"Task '{remove_task}' removed.")
            return
    print("Task not found")

def view_tasks():
    if task_items:
        print("\nTask List:")
        for index, t in enumerate(task_items):
            completion_status = "Done" if t['done'] else "Pending"
            print(f"{index + 1}. {t['task']} - {completion_status}")
    else:
        print("No tasks available.")

def mark_task_done():
    done_task = input("Enter task to mark as done: ")
    for t in task_items:
        if t['task'] == done_task:
            t['done'] = True
            print(f"Task '{done_task}' marked as done.")
            return
    print("Task not found.")

def edit_task():
    task_to_edit = input("Enter task to edit: ")
    for t in task_items:
        if t['task'] == task_to_edit:
            new_task_name = input("Enter new task name: ")
            t['task'] = new_task_name
            print(f"Task '{task_to_edit}' updated to '{new_task_name}'.")
            return
    print("Task not found.")

while True:
    show_options()
    user_choice = input("Enter your choice: ")

    if user_choice == '1':
        add_task()
    elif user_choice == '2':
        remove_task()
    elif user_choice == '3':
        view_tasks()
    elif user_choice == '4':
        mark_task_done()
    elif user_choice == '5':
        edit_task()
    elif user_choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid input. Please try again.")