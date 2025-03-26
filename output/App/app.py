Here's a Streamlit UI code that can be easily integrated with the given code:

```python
import streamlit as st
import secrets

# Define a constant for max_attempts
MAX_ATTEMPTS = 3

def get_input(prompt: str, input_type: type, max_attempts: int = MAX_ATTEMPTS) -> input_type:
    """
    Gets user input and attempts to convert it to the specified type.

    Args:
        prompt (str): The prompt to display to the user.
        input_type (type): The type to which the input should be converted.
        max_attempts (int): The maximum number of attempts to get a valid input.

    Returns:
        input_type: The user's input as the specified type.

    Raises:
        ValueError: If the input cannot be converted to the specified type after max_attempts.
    """
    attempts = 0
    while attempts < max_attempts:
        try:
            return input_type(st.text_input(prompt))
        except ValueError:
            st.error(f"Invalid input. Please enter a valid {input_type.__name__} value.")
            attempts += 1
    raise ValueError("Failed to get a valid input")

def get_random_number(min_value: int, max_value: int) -> int:
    """
    Generates a random integer between min_value and max_value (inclusive).

    Args:
        min_value (int): The minimum value for the random number.
        max_value (int): The maximum value for the random number.

    Returns:
        int: A random integer between min_value and max_value.
    """
    return secrets.randbelow(max_value - min_value + 1) + min_value

def get_random_float(min_value: float, max_value: float) -> float:
    """
    Generates a random floating-point number between min_value and max_value.

    Args:
        min_value (float): The minimum value for the random number.
        max_value (float): The maximum value for the random number.

    Returns:
        float: A random floating-point number between min_value and max_value.

    Raises:
        ValueError: If min_value is greater than max_value.
    """
    if min_value > max_value:
        raise ValueError("Minimum value cannot be greater than maximum value")
    return secrets.uniform(min_value, max_value)

def main() -> None:
    """
    The main function for the random number generator app.
    """
    st.title("Random Number Generator")
    st.write("Select an option to generate a random number.")

    option = st.selectbox("Select an option", ["Generate Random Integer", "Generate Random Float", "Quit"])

    if option == "Generate Random Integer":
        try:
            min_value = int(st.text_input("Enter minimum value: "))
            max_value = int(st.text_input("Enter maximum value: "))
            if min_value > max_value:
                st.error("Invalid range. Minimum value should be less than or equal to maximum value.")
                return
            random_number = get_random_number(min_value, max_value)
            st.write(f"Random integer: {random_number}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    elif option == "Generate Random Float":
        try:
            min_value = float(st.text_input("Enter minimum value: "))
            max_value = float(st.text_input("Enter maximum value: "))
            if min_value > max_value:
                st.error("Invalid range. Minimum value should be less than or equal to maximum value.")
                return
            random_number = get_random_float(min_value, max_value)
            st.write(f"Random float: {random_number}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    elif option == "Quit":
        st.write("Goodbye!")

if __name__ == "__main__":
    main()
```

**Explanation of Changes:**

1.  **Replaced `print` statements with Streamlit functions:** Used Streamlit functions like `st.title`, `st.write`, `st.selectbox`, `st.text_input`, and `st.error` to create a user-friendly interface.
2.  **Integrated Streamlit with the existing code:** Modified the existing code to work seamlessly with Streamlit, ensuring that the app remains functional and user-friendly.
3.  **Improved error handling:** Used `try-except` blocks to catch and display errors in a user-friendly manner, ensuring that the app remains stable and informative.
4.  **Enhanced user experience:** Added interactive elements like select boxes and text inputs to make the app more engaging and easy to use.

**Testing:**

You can test the Streamlit app by running it and selecting different options from the select box. The app should handle invalid inputs and unexpected errors, and it should generate random numbers within the specified ranges.