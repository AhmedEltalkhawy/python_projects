message =""" Enter "1" To Add Tasks 
or "2" To Complete specific task 
or "3" To view all tasks
or "4" To Quit  """
Tasks = []

def main () :
    while True :
     print(message)
     choice = input("Enter your choice :")
     if choice == "1" :
      AddTask()
     elif choice == "2" :
      MarkTaskComplete()
     elif choice == "3" :
      ViewTasks()
     else :
       break 
 
       
def AddTask() :
    task = input("Enter a task : ")
    task_info = {"task" : task , "completed" : False}
    print(task_info)
    Tasks.append(task_info)
    print("Your Task is added")

def MarkTaskComplete() :
    incomplete_tasks = []
    for task in Tasks :
        if task["completed"] == False :
            incomplete_tasks.append(task) 
    # show items to the user 
    for k , value in enumerate(incomplete_tasks) :
        print(f"entre {k+1} for {value['task']}")
    
    # take the the number of task from the user 
    task_no = int(input("enter the number of task"))
    Tasks[task_no -1]["completed"] = True
    print("this task is done ") 
    print("-"*30)
    print(Tasks)
    print("-"*30)

def ViewTasks () :
    if not Tasks :
        print("you have not any task")
        return
    for k , value in enumerate(Tasks) :
        print(f"{k+1} {value['task']}")
    print("-" * 30)

main()


