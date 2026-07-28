# To-Do List Application

tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == 2:
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks available to update.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_no = int(input("Enter task number to update: "))

            if 1 <= task_no <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[task_no - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    elif choice == 4:
        if len(tasks) == 0:
            print("No tasks available to delete.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_no = int(input("Enter task number to delete: "))

            if 1 <= task_no <= len(tasks):
                deleted_task = tasks.pop(task_no - 1)
                print(f"'{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == 5:
        print("Thank you for using the To-Do List Application!")
        break

    else:
        print("Invalid choice. Please try again.")