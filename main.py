todo_list = []

# Add Task Function
def add_task():
    task = input("Enter a task: ")
    todo_list.append({"Task": task, "Status": "pending"})
    print("New Task Added Successfully!\n")


# View Tasks Function
def view_tasks():
    print("Your Todo List:  ")
    if len(todo_list) == 0:
        print("No pending tasks!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")

# remove Tasks
def remove_task():
    if len(todo_list) == 0:
        print("List is Empty!/n")
    else:
        search_index = int(input("Enter the index of the task to remove: ")) - 1
        if 0 <= search_index < len(todo_list):
            removed_task = todo_list.pop(search_index)
            print(f"Task Removed: {removed_task['Task']}\n")
        else:
            print("Invalid task Number. Please try again.\n")

    
# Main Menu Function
def menu():
    while(True):
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
            print("Exiting the Todo List application.\n")
            exit()
            break
        else:
            print("Invalid choice. Please try again.\n")

menu()