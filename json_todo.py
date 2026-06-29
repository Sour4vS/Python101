import json
try:
    with open("tasks.json","r") as file:
        tasks = json.load(file)
        print("Welcome back! Existing tasks loaded.")



except FileNotFoundError:
    print("No previous storage file found. Initializing a clean planner...")
    tasks =[]

while True:
    print("\n" + "="*30)
    print("      PERSISTENT TASK PLANNER  ")
    print("="*30)
    print("1. View Active Tasks")
    print("2. Add a Task")
    print("3. Mark Task as Complete")
    print("4. Exit & Save")
    print("="*30)

    choice = input("enter your choice(1-4) : ").strip()
    if choice == "1":
        print("\n--- YOUR TASKS ---")
        if not tasks:
          print("\n")
          print("No tasks found! Your planner is empty.")
        else:
            for index,task_dict in enumerate(tasks, start =1):
                name = task_dict["task_name"]
                status = task_dict["status"]
                print(f"{index}. {name}[{status}]")


    elif choice == "2":
        user_input = input("what is the task description? ")
        new_task = {"task_name": user_input, "status": "Pending"}
        tasks.append(new_task)
        print("task added !")
        
   
    elif choice == "3":
        print("\n--- MARK TASK AS COMPLETE ---")
        if not tasks:
            print("You have no tasks to complete!")
        else:
            for index,task_dict in enumerate(tasks,start =1):
                print(f"{index}. {task_dict["task_name"]} [{task_dict["status"]}]")

        user_choice = int(input("Enter the number of the task completed:"))
        actual_index = user_choice - 1

        tasks[actual_index]["status"]="completed"
        print(f"\nSuccess! '{tasks[actual_index]['task_name']}' is now marked as Completed.")
        
    
    elif choice == "4":
        print("\nSaving your data and exiting...")
        with open("tasks.json","w") as file:
            json.dump(tasks,file,indent= 4)
            
        print("Data saved successfully. Goodbye!..")
        break
        
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")



