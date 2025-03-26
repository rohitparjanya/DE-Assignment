Here's a Streamlit UI code that can be easily integrated with the given code:

```python
import streamlit as st
from todo_list import ToDoList, ToDoItem, InvalidIndexError, InvalidInputError

# Initialize the to-do list
todo_list = ToDoList()

# Streamlit UI
st.title("To-Do List App")

# Add item form
with st.form("add_item"):
    title = st.text_input("Enter item title")
    description = st.text_input("Enter item description")
    submit_button = st.form_submit_button("Add Item")

    if submit_button:
        try:
            todo_list.add_item(title, description)
            st.success("Item added successfully!")
        except InvalidInputError as e:
            st.error(f"Error: {e}")

# Remove item form
with st.form("remove_item"):
    index = st.number_input("Enter item index to remove", min_value=1)
    submit_button = st.form_submit_button("Remove Item")

    if submit_button:
        try:
            todo_list.remove_item(int(index) - 1)
            st.success("Item removed successfully!")
        except InvalidIndexError as e:
            st.error(f"Error: {e}")

# Update item form
with st.form("update_item"):
    index = st.number_input("Enter item index to update", min_value=1)
    title = st.text_input("Enter new title (press enter to skip)")
    description = st.text_input("Enter new description (press enter to skip)")
    submit_button = st.form_submit_button("Update Item")

    if submit_button:
        try:
            if title == "":
                title = None
            if description == "":
                description = None
            todo_list.update_item(int(index) - 1, title, description)
            st.success("Item updated successfully!")
        except InvalidIndexError as e:
            st.error(f"Error: {e}")
        except InvalidInputError as e:
            st.error(f"Error: {e}")

# Mark item as completed form
with st.form("mark_completed"):
    index = st.number_input("Enter item index to mark as completed", min_value=1)
    submit_button = st.form_submit_button("Mark as Completed")

    if submit_button:
        try:
            todo_list.mark_item_as_completed(int(index) - 1)
            st.success("Item marked as completed!")
        except InvalidIndexError as e:
            st.error(f"Error: {e}")

# Mark item as incomplete form
with st.form("mark_incomplete"):
    index = st.number_input("Enter item index to mark as incomplete", min_value=1)
    submit_button = st.form_submit_button("Mark as Incomplete")

    if submit_button:
        try:
            todo_list.mark_item_as_incomplete(int(index) - 1)
            st.success("Item marked as incomplete!")
        except InvalidIndexError as e:
            st.error(f"Error: {e}")

# Display to-do list
if st.button("Display To-Do List"):
    st.write("To-Do List:")
    for i, item in enumerate(todo_list.items):
        st.write(f"{i+1}. {item}")
```

This Streamlit UI code provides the following features:

1.  **Add Item Form:** A form to add new items to the to-do list. It includes input fields for the title and description, and a submit button to add the item.
2.  **Remove Item Form:** A form to remove items from the to-do list. It includes an input field for the item index and a submit button to remove the item.
3.  **Update Item Form:** A form to update items in the to-do list. It includes input fields for the item index, new title, and new description, and a submit button to update the item.
4.  **Mark Item as Completed Form:** A form to mark items as completed. It includes an input field for the item index and a submit button to mark the item as completed.
5.  **Mark Item as Incomplete Form:** A form to mark items as incomplete. It includes an input field for the item index and a submit button to mark the item as incomplete.
6.  **Display To-Do List Button:** A button to display the to-do list. When clicked, it displays the to-do list with the item index, title, and description.

Note that you need to save the given code in a file named `todo_list.py` and import it in the Streamlit UI code. Also, make sure to install the required libraries, including Streamlit, by running `pip install streamlit`.