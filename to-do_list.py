def show_menu():
    print("To-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Quit")

def view_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")

def add_task(todo_list):
    task = input("Enter the task to add: ")
    todo_list.append(task)
    print("Task added successfully!")

def mark_completed(todo_list):
    view_todo_list(todo_list)
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(todo_list):
        todo_list[task_index] = f"[✓] {todo_list[task_index]}"
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def remove_task(todo_list):
    view_todo_list(todo_list)
    task_index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_index < len(todo_list):
        removed_task = todo_list.pop(task_index)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task number.")

def todo_list_app():
    todo_list = []  # Initialize an empty list for the to-do items
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            view_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            remove_task(todo_list)
        elif choice == "5":
            print("Exiting the To-Do List Application...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    todo_list_app()
