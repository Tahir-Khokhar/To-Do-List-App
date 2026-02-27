def To_do_list():
    tasks = []

    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Task")
        print("4. Quit")
        choice = int(input("Enter your choice(1/2/3/4): "))
        
        if(choice == 1):
            task = input("Enter your task: ")
            tasks.append(task)
            print(f"The {task} task is added")
        elif(choice == 2):
            task = input("Enter your task to remove: ")
            if(task in tasks):
                tasks.remove(task)
                print(f"The {task} task is removed")
            else:
                print("Task not found")
        elif(choice == 3):
            print("Task: ")
            if(task in tasks):
                print("_ " + task)
        elif(choice == 4):
            break
        else:
            print("Invalid choice")
To_do_list()
