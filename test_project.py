import pytest
from project import ToDoList, main

# Fixture to create a sample ToDoList for testing
@pytest.fixture
def sample_todo_list():
    todo_list = ToDoList()
    todo_list.add_task("Task 1", "To-Do", 0)
    todo_list.add_task("Task 2", "In Progress", 50)
    todo_list.add_task("Task 3", "Done", 100)
    return todo_list

# Test case for adding a task to ToDoList
def test_add_task(capfd):
    todo_list = ToDoList()
    todo_list.add_task("Test Task", "In Progress", 25)

    out, _ = capfd.readouterr()
    assert "Task 'Test Task' added successfully with ID" in out

# Test case for editing a task in ToDoList
def test_edit_task(capfd, sample_todo_list, monkeypatch):
    task_id = 1  # Assuming Task 1 is in the sample_todo_list
    new_name = "Updated Task"
    new_status = "Done"
    new_progress = 75

    # Prepare user input for the edit operation
    user_input = [
        "1",  # Choose the option to edit task name
        new_name,
        "2",  # Choose the option to edit task status
        new_status,
        "3",  # Choose the option to edit task progress
        str(new_progress),
        "4",  # Choose the option to cancel edit
    ]

    # Monkeypatch the input function to simulate user input
    monkeypatch.setattr("builtins.input", lambda _: user_input.pop(0))

    # Run the test for editing a task
    sample_todo_list.edit_task(task_id)

    # Check the updated task details after the edit operation
    sample_todo_list._get_task_info(task_id)

# Test case for removing a task from ToDoList
def test_remove_task(capfd, sample_todo_list):
    task_id = 2  # Assuming Task 2 is in the sample_todo_list

    # Run the test for removing a task
    sample_todo_list.remove_task(task_id)

    out, _ = capfd.readouterr()
    assert f"Task 'Task 2' with ID {task_id} removed successfully." in out

# Function to remove ANSI escape sequences from a string
def remove_ansi_escape(s):
    import re
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', s)

# Test case for exiting the program
def test_exit_program(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "0")
    with pytest.raises(SystemExit):
        main()
