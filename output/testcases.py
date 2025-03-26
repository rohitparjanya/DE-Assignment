Here's a comprehensive test case file using pytest for the given code:

```python
# tests/test_todo_list.py
import pytest
from todo_list import ToDoList, ToDoItem, InvalidIndexError, InvalidInputError

def test_todo_item_init():
    """Test initializing a ToDoItem."""
    item = ToDoItem("Test Item", "Test Description")
    assert item.title == "Test Item"
    assert item.description == "Test Description"
    assert not item.completed

def test_todo_item_mark_as_completed():
    """Test marking a ToDoItem as completed."""
    item = ToDoItem("Test Item", "Test Description")
    item.mark_as_completed()
    assert item.completed

def test_todo_item_mark_as_incomplete():
    """Test marking a ToDoItem as incomplete."""
    item = ToDoItem("Test Item", "Test Description")
    item.mark_as_completed()
    item.mark_as_incomplete()
    assert not item.completed

def test_todo_list_init():
    """Test initializing a ToDoList."""
    todo_list = ToDoList()
    assert len(todo_list.items) == 0

def test_todo_list_add_item():
    """Test adding an item to a ToDoList."""
    todo_list = ToDoList()
    todo_list.add_item("Test Item", "Test Description")
    assert len(todo_list.items) == 1

def test_todo_list_remove_item():
    """Test removing an item from a ToDoList."""
    todo_list = ToDoList()
    todo_list.add_item("Test Item", "Test Description")
    todo_list.remove_item(0)
    assert len(todo_list.items) == 0

def test_todo_list_update_item():
    """Test updating an item in a ToDoList."""
    todo_list = ToDoList()
    todo_list.add_item("Test Item", "Test Description")
    todo_list.update_item(0, "New Test Item", "New Test Description")
    assert todo_list.items[0].title == "New Test Item"
    assert todo_list.items[0].description == "New Test Description"

def test_todo_list_mark_item_as_completed():
    """Test marking an item as completed in a ToDoList."""
    todo_list = ToDoList()
    todo_list.add_item("Test Item", "Test Description")
    todo_list.mark_item_as_completed(0)
    assert todo_list.items[0].completed

def test_todo_list_mark_item_as_incomplete():
    """Test marking an item as incomplete in a ToDoList."""
    todo_list = ToDoList()
    todo_list.add_item("Test Item", "Test Description")
    todo_list.mark_item_as_completed(0)
    todo_list.mark_item_as_incomplete(0)
    assert not todo_list.items[0].completed

def test_todo_list_invalid_index():
    """Test handling an invalid index in a ToDoList."""
    todo_list = ToDoList()
    with pytest.raises(InvalidIndexError):
        todo_list.remove_item(0)

def test_todo_list_invalid_input():
    """Test handling invalid input in a ToDoList."""
    todo_list = ToDoList()
    with pytest.raises(InvalidInputError):
        todo_list.add_item("Test Item!", "Test Description")

def test_todo_list_update_item_invalid_input():
    """Test handling invalid input when updating an item in a ToDoList."""
    todo_list = ToDoList()
    todo_list.add_item("Test Item", "Test Description")
    with pytest.raises(InvalidInputError):
        todo_list.update_item(0, "New Test Item!", "New Test Description")

def test_todo_list_update_item_invalid_index():
    """Test handling an invalid index when updating an item in a ToDoList."""
    todo_list = ToDoList()
    with pytest.raises(InvalidIndexError):
        todo_list.update_item(0, "New Test Item", "New Test Description")

def test_todo_list_mark_item_as_completed_invalid_index():
    """Test handling an invalid index when marking an item as completed in a ToDoList."""
    todo_list = ToDoList()
    with pytest.raises(InvalidIndexError):
        todo_list.mark_item_as_completed(0)

def test_todo_list_mark_item_as_incomplete_invalid_index():
    """Test handling an invalid index when marking an item as incomplete in a ToDoList."""
    todo_list = ToDoList()
    with pytest.raises(InvalidIndexError):
        todo_list.mark_item_as_incomplete(0)

# Test fixtures
@pytest.fixture
def todo_list():
    return ToDoList()

@pytest.fixture
def todo_item():
    return ToDoItem("Test Item", "Test Description")

# Test parameterization
@pytest.mark.parametrize("title, description", [
    ("Test Item", "Test Description"),
    ("New Test Item", "New Test Description"),
])
def test_todo_item_init_parameterized(title, description):
    """Test initializing a ToDoItem with different parameters."""
    item = ToDoItem(title, description)
    assert item.title == title
    assert item.description == description
    assert not item.completed

# Test setup and teardown
def test_todo_list_setup_teardown():
    """Test setting up and tearing down a ToDoList."""
    todo_list = ToDoList()
    try:
        todo_list.add_item("Test Item", "Test Description")
        assert len(todo_list.items) == 1
    finally:
        todo_list.remove_item(0)
        assert len(todo_list.items) == 0
```

This test case file covers various scenarios, including:

1.  Initializing a `ToDoItem` and a `ToDoList`.
2.  Adding, removing, updating, and marking items as completed or incomplete in a `ToDoList`.
3.  Handling invalid input and indices in a `ToDoList`.
4.  Using test fixtures to create a `ToDoList` and a `ToDoItem`.
5.  Using test parameterization to test initializing a `ToDoItem` with different parameters.
6.  Using test setup and teardown to test setting up and tearing down a `ToDoList`.

These tests ensure that the `ToDoList` and `ToDoItem` classes are working correctly and handle various scenarios as expected.