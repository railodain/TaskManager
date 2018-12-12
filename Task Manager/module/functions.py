from classes import TaskInventory

# Main chat function
def start_working():
    "Prints various methods of TaskInventory given input messages."
    
    # An instance of TaskInventory 
    my_tasks = TaskInventory()
    
    # Variable decides whether work session continues or not
    user_working = True
    while user_working:   
        
        # Default message
        message = input("""\nWhat would you like to do? \n 
        - Input task \n
        - Mark task completed \n
        - Get schedule \n 
        - Get recommended task \n
        - Rest for now \n\n""")
        
        # Conditional for adding new tasks
        if message.lower() == "input task":
            task_name = input("\nWhat is the name of your task? \n")
            task_due_date = input("What date is your task due? (dd/mm/yy) \n")
            task_amt_time = input("How many hours will it take? \n")
            task_difficulty = input("Is this task easy, or hard to focus on? \n")            
            
            my_tasks.add_task(task_name, task_due_date, task_amt_time, task_difficulty)
       
        # Conditional for removing completed tasks
        if message.lower() == "mark task completed":
            completed_task = input("\n What task did you finish? (Case Sensitive) \n")
            
            my_tasks.delete_task(completed_task)
            print("\nLook at you go!")
    
        # Conditional for printing a schedule of tasks, by order of due date
        if message.lower() == "get schedule":
            my_tasks.print_schedule()
 
        # Conditional for printing recommended task
        if message.lower() == "get recommended task":
            mood = input("\nAre you feeling focused, or unfocused? \n")
            
            print("\nSince you're feeling {}, I recommend you work on your task '{}'.".format(mood.lower(), my_tasks.recommend_task(mood)))

        # Conditional for ending work session
        if message.lower() == "rest for now":
            print("\nGreat work!")
            user_working = False
        
