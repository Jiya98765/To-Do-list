FILENAME = "tasks.txt"   

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []  


def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


tasks = load_tasks()

def show_menu():
    print("\n =====list======")
    print("1. Add your task : ")
    print("2. View lest : ")
    print("3. Delete task : ")
    print("4. Exit ")

while True :
    show_menu()
    choice = input("Enter your choice(1-4) : ")

    if choice == '1':
        task = input("Enter your task : ")
        tasks.append(task)
        save_tasks(tasks)
        print(f" '{task}' added Succesfully")

    elif choice == '2':
        print("\nYour tasks :")
        if not tasks :
            print("No tasks yet !")
        else :
            for i , t in enumerate(tasks , start=1):
                print(f"{i} . {t}")
    
    elif choice == '3' :
        if not tasks :
            print("NO task to delete !")
        else :
            num = int(input("Enter your task number to Delete : "))

            if 0 < num <= len(tasks):
                removed = tasks.pop(num-1)
                save_tasks(tasks)
                print(f" '{removed}' delete.")
            
            else :
                print("X Invalid task number !")
    
    elif choice == '4' :
        print("Goodbye !")
        break 

    else :
        print("Invalid Choice Try Again .")