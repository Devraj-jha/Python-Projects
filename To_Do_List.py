#Building a terminal based to do list that can add or view tasks 
tasks = []
def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter choice (1-3): ")

        if choice == '1':
            task = input("Enter your task: ")
            tasks.append(task)
            print(f"{task} Added !!")

        elif choice == '2':
            print("----Your Tasks----") 
            if not task:
                print("empty")
            for i, task in enumerate(tasks, 1):
                print(f"{i} {task}")
        elif choice == '3':
            if not tasks:
                print("There is not thing delete")
            else:
                print("<--- Task to delete --->") 
                for i,task in enumerate(tasks, 1):
                    print(f"{i} {task}")
                
                try:
                    task_num = int(input("Enter task number to delete:  "))
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"{i} {removed_task} removed sucessfully")

                    else:
                        print(f"invaid number enter between 1 and {len(tasks)}")

                except ValueError:
                    print("Invaid input please enter a number ")

        elif choice == '4':
            print(" Good bye ")
            break
        
        else:
            print("Enter something vaild")

main()