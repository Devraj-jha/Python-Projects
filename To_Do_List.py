#Building a terminal based to do list that can add or view tasks 
tasks = []
def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

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
            print(" Good bye ")
            break
        
        else:
            print("Enter something vaild")

main()