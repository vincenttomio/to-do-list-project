# To-Do List Project  

### Description  
The **To-Do List Project** is a simple console-based application implemented in Python, designed to manage tasks efficiently. Users can add, edit, remove, and view tasks through a text-based menu interface.  

The project consists of two main files:  
- **`project.py`**: Contains the implementation of the To-Do List application.  
- **`test_project.py`**: Contains test cases to ensure the application's functionalities work as expected.  

---

## Files  

### `project.py`  
#### Class: `ToDoList`  
- Core functionality of the To-Do List application.  
- Includes methods for managing tasks and interacting with the user via a console interface.  
- Utilizes ANSI escape codes for enhanced console text formatting.  

#### Methods  
- **`generate_task_id`**: Generates unique task IDs.  
- **`add_task`**: Adds a new task with name, status, and progress.  
- **`edit_task`**: Allows editing task details. Includes helper methods like:  
  - `_edit_task_name`, `_edit_task_status`, `_edit_task_progress`.  
  - `_cancel_edit` and `_invalid_edit_option` handle cancellations and invalid inputs.  
- **`remove_task`**: Deletes tasks by ID.  
- **`view_tasks`**: Displays all tasks in a formatted manner.  

#### Functions  
- **`menu_display`**: Displays the main menu options.  
- **`exit_program`**: Handles application termination.  
- **`main`**: Executes the To-Do List application.  

---

### `test_project.py`  
#### Test Cases  
- **`test_add_task`**: Validates the functionality of adding new tasks.  
- **`test_edit_task`**: Tests editing existing tasks.  
- **`test_remove_task`**: Ensures tasks can be removed correctly.  
- **`test_exit_program`**: Tests the application’s exit functionality.  

---

## How to Run  
1. Ensure Python is installed on your system. 

2. Clone the repository:  
   ```bash  
   git clone https://github.com/YourUsername/to-do-list-project.git
   ```

3. Navigate to the project directory:
    ```bash
   cd to-do-list-project  
   ```

4. Run the application:
    ```bash
   python project.py  
   ```

5. Follow the on-screen menu to manage tasks.

## Running Tests  

- To run the test cases:
    ```bash
    pytest test_project.py  
    ```

## Certificate of Completion  
This project is part of the **CS50’s Introduction to Programming with Python** [here](https://cs50.harvard.edu/python/2022/) course by Harvard University.  

You can view the certificate of completion [here](CS50P_certificate.pdf).  

---

## Dependencies  
No external dependencies are required. The project runs on standard Python libraries.  

---

## Author  
**Vincent Tomio**  
Feel free to use, modify, or extend the To-Do List Project for personal or educational purposes.  

For questions or suggestions, please open an issue in the repository or contact me directly.  
