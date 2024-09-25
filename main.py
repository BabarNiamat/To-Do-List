import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks, task):
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)

def view_tasks(tasks):
    for index, task in enumerate(tasks):
        status = '✔️' if task['completed'] else '❌'
        print(f"{index + 1}. {task['task']} [{status}]")

def update_task(tasks, index, new_task):
    if 0 <= index < len(tasks):
        tasks[index]['task'] = new_task
        save_tasks(tasks)

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

def mark_as_complete(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        save_tasks(tasks)

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task description: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter new task description: ")
            update_task(tasks, index, new_task)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == '5':
            index = int(input("Enter task number to mark as complete: ")) - 1
            mark_as_complete(tasks, index)
        elif choice == '6':
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
