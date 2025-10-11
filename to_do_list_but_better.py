import os
TODO_FILE = "todo.txt"
def load_task():
    tasks = []

    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            for line in file:
                task = line.strip()
                if task: 
                    tasks.append(task)
    return tasks

def save_tasks(tasks):


    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def show_tasks(tasks):
    if not tasks:
        print("Your to do list is empty")
    
    else: 
        print("your to do list: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}) { task}")


def add_task(tasks):
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added.")

    else:
        print("task can't be empty")

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            task_num= int(input("enter your number to delete"))
            if 1 <= task_num <= len(tasks):
                removed_task = task.pop(task)
                