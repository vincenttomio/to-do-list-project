class ToDoList:
    # ANSI escape codes for text colors
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"

    def __init__(self):
        # Initialize ToDoList with an empty task dictionary and a starting task ID
        self.tasks = {}
        self.current_task_id = 1

    def generate_task_id(self):
        # Generate a unique task ID and increment the current_task_id
        task_id = self.current_task_id
        self.current_task_id += 1
        return task_id

    def add_task(self, task_name, status="To-Do", progress=0):
        # Add a new task to the task dictionary with a generated task ID
        task_id = self.generate_task_id()
        self.tasks[task_id] = {"name": task_name, "status": status, "progress": progress}
        # Print a success message with ANSI color formatting
        print(f"{self.GREEN}Task '{task_name}' added successfully with ID {task_id}.{self.RESET}")

    def edit_task(self, task_id, user_input=None):
        # Edit an existing task based on user input
        if task_id in self.tasks:
            print(f"\n{self.BLUE}Editing Task with ID {task_id}: {self.tasks[task_id]['name']}{self.RESET}")

            # Define edit options and corresponding functions
            edit_options = {
                1: self._edit_task_name,
                2: self._edit_task_status,
                3: self._edit_task_progress,
                4: self._cancel_edit
            }

            # Display available edit options to the user
            for option, function in edit_options.items():
                print(f"{option}. {function.__name__.replace('_edit_task_', '').capitalize()}")

            try:
                # Get the user's edit choice, either from input or pre-defined user input
                if user_input is None:
                    edit_choice = int(input("Enter the number of the desired edit option: "))
                else:
                    edit_choice = int(user_input.pop(0))
            except ValueError:
                print("Invalid input. Please enter a number.")
                return

            # Execute the selected edit option on the task
            edit_options.get(edit_choice, self._invalid_edit_option)(task_id)

        else:
            print(f"{self.RED}The task with ID {task_id} does not exist in the list.{self.RESET}")

    def _edit_task_name(self, task_id):
        # Edit the name of a task
        new_name = input(f"{self.GREEN}Enter the new task name: {self.RESET}")
        self.tasks[task_id]['name'] = new_name
        print(f"{self.GREEN}Task name updated successfully.{self.RESET}")

    def _edit_task_status(self, task_id):
        # Edit the status of a task
        new_status = input(f"{self.YELLOW}Enter the new task status: {self.RESET}")
        self.tasks[task_id]['status'] = new_status
        print(f"{self.YELLOW}Task status updated successfully.{self.RESET}")

    def _edit_task_progress(self, task_id):
        # Edit the progress of a task
        new_progress = int(input(f"{self.BLUE}Enter the new progress percentage (0-100): {self.RESET}"))
        self.tasks[task_id]['progress'] = new_progress
        print(f"{self.BLUE}Task progress updated successfully.{self.RESET}")

    def _cancel_edit(self, task_id):
        # Cancel the edit operation
        print("Edit canceled.")

    def _invalid_edit_option(self, task_id):
        # Display an error message for an invalid edit option
        print("Invalid edit option. Please try again.")

    def _get_task_info(self, task_id):
        # Display detailed information about a task
        if task_id in self.tasks:
            info = self.tasks[task_id]
            print(f"Task ID: {task_id}")
            print(f"Task Name: {info['name']}")
            print(f"Task Status: {info['status']}")
            print(f"Task Progress: {info['progress']}%")
        else:
            print(f"{self.RED}The task with ID {task_id} does not exist in the list.{self.RESET}")

    def remove_task(self, task_id):
        # Remove a task from the task dictionary
        if task_id in self.tasks:
            task_name = self.tasks[task_id]['name']
            self.tasks.pop(task_id)
            print(f"{self.RED}Task '{task_name}' with ID {task_id} removed successfully.{self.RESET}")
        else:
            print(f"{self.RED}The task with ID {task_id} does not exist in the list.{self.RESET}")

    def view_tasks(self):
        # Display a formatted view of all tasks in the task dictionary
        if not self.tasks:
            print(f"{self.BLUE}The task list is empty.{self.RESET}")
        else:
            print(f"\n{self.BLUE}Task List:{self.RESET}")
            print("-" * 76)
            print(f"| {'ID':<3} | {'Task':<30} | {'Status':<15} | {'Progress (%)':<15} |")
            print("-" * 76)
            for task_id, info in self.tasks.items():
                print(f"| {task_id:<3} | {info['name']:<30} | {info['status']:<15} | {info['progress']:<15} |")
            print("-" * 76)


# Function to display the main menu of the ToDoList application
def menu_display():
    red = ToDoList.RED
    green = ToDoList.GREEN
    yellow = ToDoList.YELLOW
    blue = ToDoList.BLUE
    reset = ToDoList.RESET

    print("\n" + red + "-" * 25)
    print("     To-Do List Menu")
    print("-" * 25 + reset)
    print(f"{green}1. Add Task")
    print(f"{yellow}2. Edit Task")
    print(f"3. Remove Task")
    print(f"{blue}4. View Tasks")
    print(f"{red}0. Exit")
    print("-" * 25 + reset)


# Function to handle program exit
def _exit_program():
    print("Exiting the program.")
    raise SystemExit


# Main function to run the ToDoList application
def main():
    todo_list = ToDoList()

    while True:
        menu_display()

        try:
            choice = int(input("Enter the number of the desired option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            # Add a new task based on user input
            task_name = input(f"{ToDoList.GREEN}Enter the new task: {ToDoList.RESET}")
            status = input(f"{ToDoList.YELLOW}Enter the status (e.g., 'To-Do', 'In Progress', 'Done'): {ToDoList.RESET}")
            progress = int(input(f"{ToDoList.BLUE}Enter the progress percentage (0-100): {ToDoList.RESET}"))
            todo_list.add_task(task_name, status, progress)
        elif choice in [2, 3]:
            # Edit or remove a task based on user input
            task_id = int(input(f"Enter the ID of the task to be {'edited' if choice == 2 else 'removed'}: "))
            if choice == 2:
                todo_list.edit_task(task_id)
            else:
                todo_list.remove_task(task_id)
        elif choice == 4:
            # View all tasks
            todo_list.view_tasks()
        elif choice == 0:
            # Exit the program
            _exit_program()
        else:
            print("Invalid option. Please try again.")


# Run the ToDoList application if the script is executed directly
if __name__ == "__main__":
    main()
