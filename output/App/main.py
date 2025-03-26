import re
import unittest

# Custom exception classes
class ToDoListError(Exception):
    pass

class InvalidIndexError(ToDoListError):
    pass

class InvalidInputError(ToDoListError):
    pass

class ToDoItem:
    """Represents a single to-do list item."""
    def __init__(self, title, description, completed=False):
        """
        Initializes a new to-do list item.

        Args:
            title (str): The title of the item.
            description (str): The description of the item.
            completed (bool, optional): Whether the item is completed. Defaults to False.

        Raises:
            InvalidInputError: If the title or description is invalid.
        """
        if not re.match(r"^[a-zA-Z0-9\s]+$", title):
            raise InvalidInputError("Invalid title")
        if not re.match(r"^[a-zA-Z0-9\s]+$", description):
            raise InvalidInputError("Invalid description")

        self.title = title
        self.description = description
        self.completed = completed

    def mark_as_completed(self):
        """Marks the item as completed."""
        self.completed = True

    def mark_as_incomplete(self):
        """Marks the item as incomplete."""
        self.completed = False

    def __str__(self):
        """Returns a string representation of the item."""
        status = "Completed" if self.completed else "Incomplete"
        return f"{self.title}: {status}\nDescription: {self.description}"


class ToDoList:
    """Represents a to-do list."""
    def __init__(self):
        """Initializes a new to-do list."""
        self.items = []

    def add_item(self, title, description):
        """
        Adds a new item to the list.

        Args:
            title (str): The title of the item.
            description (str): The description of the item.

        Raises:
            InvalidInputError: If the title or description is invalid.
        """
        try:
            new_item = ToDoItem(title, description)
            self.items.append(new_item)
        except InvalidInputError as e:
            raise InvalidInputError(f"Failed to add item: {e}")

    def remove_item(self, index):
        """
        Removes an item from the list.

        Args:
            index (int): The index of the item to remove.

        Raises:
            InvalidIndexError: If the index is invalid.
        """
        try:
            del self.items[index]
        except IndexError:
            raise InvalidIndexError("Invalid index")

    def update_item(self, index, title=None, description=None):
        """
        Updates an item in the list.

        Args:
            index (int): The index of the item to update.
            title (str, optional): The new title of the item. Defaults to None.
            description (str, optional): The new description of the item. Defaults to None.

        Raises:
            InvalidIndexError: If the index is invalid.
            InvalidInputError: If the title or description is invalid.
        """
        try:
            item = self.items[index]
            if title:
                if not re.match(r"^[a-zA-Z0-9\s]+$", title):
                    raise InvalidInputError("Invalid title")
                item.title = title
            if description:
                if not re.match(r"^[a-zA-Z0-9\s]+$", description):
                    raise InvalidInputError("Invalid description")
                item.description = description
        except IndexError:
            raise InvalidIndexError("Invalid index")

    def mark_item_as_completed(self, index):
        """
        Marks an item as completed.

        Args:
            index (int): The index of the item to mark as completed.

        Raises:
            InvalidIndexError: If the index is invalid.
        """
        try:
            self.items[index].mark_as_completed()
        except IndexError:
            raise InvalidIndexError("Invalid index")

    def mark_item_as_incomplete(self, index):
        """
        Marks an item as incomplete.

        Args:
            index (int): The index of the item to mark as incomplete.

        Raises:
            InvalidIndexError: If the index is invalid.
        """
        try:
            self.items[index].mark_as_incomplete()
        except IndexError:
            raise InvalidIndexError("Invalid index")

    def display_list(self):
        """Displays the to-do list."""
        for i, item in enumerate(self.items):
            print(f"{i+1}. {item}")


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update item")
        print("4. Mark item as completed")
        print("5. Mark item as incomplete")
        print("6. Display list")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter item title: ")
            description = input("Enter item description: ")
            try:
                todo_list.add_item(title, description)
            except InvalidInputError as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                index = int(input("Enter item index to remove: ")) - 1
                todo_list.remove_item(index)
            except InvalidIndexError as e:
                print(f"Error: {e}")
        elif choice == "3":
            try:
                index = int(input("Enter item index to update: ")) - 1
                title = input("Enter new title (press enter to skip): ")
                description = input("Enter new description (press enter to skip): ")
                if title == "":
                    title = None
                if description == "":
                    description = None
                todo_list.update_item(index, title, description)
            except InvalidIndexError as e:
                print(f"Error: {e}")
            except InvalidInputError as e:
                print(f"Error: {e}")
        elif choice == "4":
            try:
                index = int(input("Enter item index to mark as completed: ")) - 1
                todo_list.mark_item_as_completed(index)
            except InvalidIndexError as e:
                print(f"Error: {e}")
        elif choice == "5":
            try:
                index = int(input("Enter item index to mark as incomplete: ")) - 1
                todo_list.mark_item_as_incomplete(index)
            except InvalidIndexError as e:
                print(f"Error: {e}")
        elif choice == "6":
            todo_list.display_list()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


class TestToDoList(unittest.TestCase):
    def test_add_item(self):
        todo_list = ToDoList()
        todo_list.add_item("Test Item", "Test Description")
        self.assertEqual(len(todo_list.items), 1)

    def test_remove_item(self):
        todo_list = ToDoList()
        todo_list.add_item("Test Item", "Test Description")
        todo_list.remove_item(0)
        self.assertEqual(len(todo_list.items), 0)

    def test_update_item(self):
        todo_list = ToDoList()
        todo_list.add_item("Test Item", "Test Description")
        todo_list.update_item(0, "New Test Item", "New Test Description")
        self.assertEqual(todo_list.items[0].title, "New Test Item")
        self.assertEqual(todo_list.items[0].description, "New Test Description")

    def test_mark_item_as_completed(self):
        todo_list = ToDoList()
        todo_list.add_item("Test Item", "Test Description")
        todo_list.mark_item_as_completed(0)
        self.assertTrue(todo_list.items[0].completed)

    def test_mark_item_as_incomplete(self):
        todo_list = ToDoList()
        todo_list.add_item("Test Item", "Test Description")
        todo_list.mark_item_as_completed(0)
        todo_list.mark_item_as_incomplete(0)
        self.assertFalse(todo_list.items[0].completed)

if __name__ == "__main__":
    unittest.main(exit=False)
    main()