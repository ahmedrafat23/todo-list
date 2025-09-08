
---

## 📄 `todo.py`
```python
# Simple To-Do List App

tasks = []  # empty list to store tasks

while True:
    print("\n--- To-Do List ---")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as done")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")
    elif choice == "2":
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif choice == "3":
        if not tasks:
            print("No tasks to mark as done!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                done = int(input("Enter the task number to mark as done: "))
                if 1 <= done <= len(tasks):
                    finished = tasks.pop(done - 1)
                    print(f"Task '{finished}' marked as done and removed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1-4.")
