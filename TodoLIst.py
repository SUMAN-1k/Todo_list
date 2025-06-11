def show_menu():
    print("\n======TODO LIST MENU========")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark as completed ")
    print("4. Delete Task")
    print("5. Exit")

tasks=[]

def add_task():
    task=input("Enter the task: ")
    tasks.append({'task':task,'completed':False})
    print("✅ Task added successfully!")

def view_task():
    if not tasks:
        print("📭 No tasks to show.")
        return
    print("\n📋 Your Tasks:")
    for idx,task in enumerate(tasks,1):
        status="✅ Done" if task['completed'] else "⏳ Pending"
        print(f"{idx}.{task['task']} [{status}]")

def mark_completed():
    view_task()
    try:
        task_no=int(input("enter the task number to mark as completed:"))
        if 1<=task_no<=len(tasks):
            tasks[task_no-1]['completed']=True
            print("🎉 Task marked as completed.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

def delete_task():
    view_task()
    try:
        task_no=int(input("enter the task number to be delete: "))
        if 1<=task_no<=len(tasks):
            deleted=tasks.pop(task_no-1)
            print(f"🗑️ Deleted task: {deleted['task']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")


while True:
    show_menu()
    choice=input("Enter your choice (1-5): ")

    if choice=='1':
        add_task()
    elif choice=='2':
        view_task()
    elif choice=='3':
        mark_completed()
    elif choice=='4':
        delete_task()
    elif choice=='5':
        print("👋 Goodbye!")
        break
    else:
        print('⚠️ Invalid choice. Please try again.')