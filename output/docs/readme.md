# To-Do List Application
==========================

## Overview
-----------

The To-Do List Application is a simple Python program that allows users to create, manage, and track their to-do lists. The application provides a menu-driven interface for users to add, remove, update, and mark items as completed or incomplete.

## Installation
------------

To install the To-Do List Application, follow these steps:

1. **Clone the repository**: Clone the repository containing the To-Do List Application code.
2. **Install Python**: Ensure that you have Python installed on your system. You can download the latest version of Python from the official Python website.
3. **Run the application**: Navigate to the directory containing the To-Do List Application code and run the `main.py` file using Python.

## Usage
-----

To use the To-Do List Application, follow these steps:

1. **Launch the application**: Run the `main.py` file using Python.
2. **Menu options**: The application will display a menu with the following options:
	* Add item
	* Remove item
	* Update item
	* Mark item as completed
	* Mark item as incomplete
	* Display list
	* Quit
3. **Select an option**: Enter the number corresponding to the option you want to select.
4. **Follow prompts**: The application will prompt you to enter the required information, such as the item title and description.

### Adding an Item

To add an item to the to-do list, follow these steps:

1. **Select the "Add item" option**: Enter `1` to select the "Add item" option.
2. **Enter the item title**: Enter the title of the item you want to add.
3. **Enter the item description**: Enter the description of the item you want to add.
4. **Confirm**: The application will add the item to the to-do list and display a confirmation message.

### Removing an Item

To remove an item from the to-do list, follow these steps:

1. **Select the "Remove item" option**: Enter `2` to select the "Remove item" option.
2. **Enter the item index**: Enter the index of the item you want to remove.
3. **Confirm**: The application will remove the item from the to-do list and display a confirmation message.

### Updating an Item

To update an item in the to-do list, follow these steps:

1. **Select the "Update item" option**: Enter `3` to select the "Update item" option.
2. **Enter the item index**: Enter the index of the item you want to update.
3. **Enter the new title**: Enter the new title of the item (optional).
4. **Enter the new description**: Enter the new description of the item (optional).
5. **Confirm**: The application will update the item in the to-do list and display a confirmation message.

### Marking an Item as Completed or Incomplete

To mark an item as completed or incomplete, follow these steps:

1. **Select the "Mark item as completed" or "Mark item as incomplete" option**: Enter `4` to select the "Mark item as completed" option or `5` to select the "Mark item as incomplete" option.
2. **Enter the item index**: Enter the index of the item you want to mark as completed or incomplete.
3. **Confirm**: The application will mark the item as completed or incomplete and display a confirmation message.

## API Reference
--------------

The To-Do List Application provides the following classes and methods:

### `ToDoItem` Class

* `__init__(title, description, completed=False)`: Initializes a new to-do list item.
* `mark_as_completed()`: Marks the item as completed.
* `mark_as_incomplete()`: Marks the item as incomplete.
* `__str__()`: Returns a string representation of the item.

### `ToDoList` Class

* `__init__()`: Initializes a new to-do list.
* `add_item(title, description)`: Adds a new item to the list.
* `remove_item(index)`: Removes an item from the list.
* `update_item(index, title=None, description=None)`: Updates an item in the list.
* `mark_item_as_completed(index)`: Marks an item as completed.
* `mark_item_as_incomplete(index)`: Marks an item as incomplete.
* `display_list()`: Displays the to-do list.

## Testing
---------

The To-Do List Application includes unit tests to ensure that it is working correctly. The tests cover various scenarios, including adding, removing, updating, and marking items as completed or incomplete.

To run the tests, navigate to the directory containing the To-Do List Application code and run the `unittest` module using Python.

## Troubleshooting
-----------------

If you encounter any issues while using the To-Do List Application, refer to the following troubleshooting guide:

* **Invalid input**: Ensure that you are entering valid input, such as numbers for indices and strings for titles and descriptions.
* **Item not found**: Ensure that the item you are trying to remove or update exists in the to-do list.
* **Application crashes**: Try restarting the application or checking for any syntax errors in the code.

## Conclusion
----------

The To-Do List Application is a simple and easy-to-use program that allows users to create, manage, and track their to-do lists. With its menu-driven interface and robust error handling, the application provides a user-friendly experience for managing to-do lists.