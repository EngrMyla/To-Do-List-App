todo_list = []

# Add Task Function
def add_task():
    task = input("Enter a task: ")
    todo_list.append({"Task": task, "Status": "pending"})
    print("New task added successfully!\n")


# View Tasks Function
def view_tasks():
    print("Your Todo List:  ")
    if len(todo_list) == 0:
        print("No pending tasks!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")

# Remove Tasks
def remove_task():
    if len(todo_list) == 0:
        print("List is empty!\n")
    else:
        try:
            search_index = int(input("Enter the index of the task to remove: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task Removed: {removed_task['Task']}\n")
            else:
                print("Invalid task number. Please try again.\n")
        except ValueError:
            print("Invalid task number. Please try a valid task number.\n")

# Marking Task as Completed
def mark_done():
    if len(todo_list) == 0:
        print("List is Empty!\n")
    else:
        try:
            search_index = int(input("Enter the index of the task that you want to mark as completed: ")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['Status'] = 'done'
                print(f"Task {todo_list[search_index]['Task']} marked as completed.\n")
            else:
                print("Invalid task number. Please try again.\n")
        except ValueError:
            print("Invalid task number. Please try a valid task number.\n")

# Main Menu Function
def menu():
    while True:
        print("Todo List Menu:")
        print("1. Add a New Task")
        print("2. View All Tasks")
        print("3. Remove a Task")
        print("4. Mark a Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_done()
        elif choice == '5':
            print("Exiting...\n")
            exit()
        else:
            print("Invalid choice. Please try again.\n")

menu()