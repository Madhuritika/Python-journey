tasks = []

def add_task():
    task = input("Enter your task: ")
    return task
for i in range(3):#to add  three tasks
    print(f"Task {i+1}:")
    tasks.append(add_task())
print("\nYour To-Do List:") 
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
