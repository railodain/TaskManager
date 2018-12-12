class TaskInventory():
    """Stores a list of tasks with their description.
    
    Attributes
    ----------
    tasks : list
        List of dictionaries describing each task.
    
    Methods
    -------
    add_task :
        Adds dictionaries to the list 'tasks'.
    delete_task :
        Removes the dictionary corresponding to an inputed name from list 'tasks'.
    order_due :
        Sorts list 'tasks' by due date.
    print_schedule : 
        Prints the name of each task headed by its due date.
    difficulty :
        Divides items in list 'tasks' into lists 'hard_tasks' and 'easy_tasks'.
    recommend_task : 
        Returns recommended task.
    """
    
    
    def __init__(self):
        self.tasks = []
    
    
    # Allows user to add tasks to their instance of TaskInventory
    def add_task(self, name, due_date, amt_time, difficulty):
        """Files inputs into a dictionary, which appends to list 'tasks'.
        
        Parameters
        ----------
        name : string
            String containing task name
        due_date : string
            String in format dd/mm/yy containing task due date
        amt_time : string
            String containing number of hours tasks takes
        difficulty: string
            String with possible inputs 'easy' and 'hard'
        """
        
        about_task = {
            "name": name,
            "due_date": due_date,
            "amt_time": amt_time,
            "difficulty": difficulty
        }
        
        self.tasks.append(about_task)
        

    
    # Deletes a task from 'tasks'
    def delete_task(self, name):
        """Loops through 'tasks' and removes the one whose 'name' item corresponds to an input.

        Parameters
        ----------
        name : string
            String containing task name to delete
        """
        for task in self.tasks:
            if task['name'] == name:
                self.tasks.remove(task)
            else:
                pass
        

    # Sorts tasks by due date to all user to access the first task due, and a schedule of tasks.
    def order_due(self):
        """Orders 'tasks' by the number of days between each tasks' due date and today's date.

        Returns
        -------
        ordered_tasks : list
            Tasks are sorted by the number of days between their due date and today's date.
        """
        from datetime import date

        # Returns the number of days between a given date in dd/mm/yy format, and todays date.
        def days_from_today(my_date):

            day = int(my_date[3:5])
            month = int(my_date[:2])
            year = int("20" + my_date[6:])

            d1 = date(year, month, day)
            d2 = date.today()

            difference = (d1 - d2).days

            return difference

        # Sorts the list 'tasks' by how far its due dates are from today.
        ordered_tasks = sorted(self.tasks, key=lambda k: days_from_today(k['due_date']))

        return ordered_tasks

 

    # Prints tasks with their due dates
    def print_schedule(self):
        "Prints tasks in self.orderdue() as their date followed by their name."
        
        if self.order_due() != []:
            for task in self.order_due():
                print(task['due_date'])
                print(task['name'] + ": " + task['amt_time'] + " hours")
                print( ) # Blank line
        
        # A message incase there are no tasks in 'tasks'.
        if self.order_due() == []:
            print("\nYou have no tasks! Input more, or enjoy some well-deserved rest. \n")
        
        
    # Sorts tasks into easy tasks and a hard tasks.
    def difficulty(self):
        """Appends dictionaries in 'tasks' to list 'easy_task' if task is easy, and 'hard_task' if task is hard.
        
        Returns
        -------
        easy_tasks : list
            All dictionaries in 'self.order_due()' with value 'easy' for key 'difficulty'.
        hard_tasks : list
            All dictionaries in 'self.order_due()' with value 'hard' for key 'difficulty'.
        """
        easy_tasks = []
        hard_tasks = []

        for task in self.order_due():
            if task["difficulty"].lower() == 'easy':
                easy_tasks.append(task)
            if task["difficulty"].lower() == 'hard':
                hard_tasks.append(task)

        return easy_tasks, hard_tasks
    
    
    # Recommends user a task based on their given  
    def recommend_task(self, user_mood):
        """Returns the first item in easy_tasks, or the first task in hard_tasks.
        
        Parameters
        ----------
        user_mood : string
            Either "focused" or "unfocused".
        
        Returns
        -------
        recommended_task : string
            Name of first item in easy_tasks or hard_tasks, depending on value of user_mood.
        """
        easy_tasks, hard_tasks = self.difficulty()

        recommended_task = ""

        if user_mood.lower() == "focused":
            recommended_task = hard_tasks[0]['name']
        if user_mood.lower() == "unfocused":
            recommended_task = easy_tasks[0]['name']

        return recommended_task
