import secrets
import unittest

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
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__} value.")
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

def display_menu() -> None:
    """
    Displays the menu for the random number generator app.
    """
    print("Random Number App")
    print("----------------")

def generate_random_integer() -> None:
    """
    Generates a random integer within a user-specified range.
    """
    try:
        min_value = get_input("Enter minimum value: ", int)
        max_value = get_input("Enter maximum value: ", int)
        if min_value > max_value:
            print("Invalid range. Minimum value should be less than or equal to maximum value.")
            return
        random_number = get_random_number(min_value, max_value)
        print(f"Random integer: {random_number}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def generate_random_float() -> None:
    """
    Generates a random floating-point number within a user-specified range.
    """
    try:
        min_value = get_input("Enter minimum value: ", float)
        max_value = get_input("Enter maximum value: ", float)
        if min_value > max_value:
            print("Invalid range. Minimum value should be less than or equal to maximum value.")
            return
        random_number = get_random_float(min_value, max_value)
        print(f"Random float: {random_number}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main() -> None:
    """
    The main function for the random number generator app.
    """
    display_menu()
    while True:
        print("1. Generate random integer")
        print("2. Generate random float")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_random_integer()
        elif choice == "2":
            generate_random_float()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

class TestRandomNumberGenerator(unittest.TestCase):
    def test_get_input(self):
        # Test get_input with valid input
        self.assertEqual(get_input("Enter a number: ", int), 10)

        # Test get_input with invalid input
        with self.assertRaises(ValueError):
            get_input("Enter a number: ", int)

    def test_get_random_number(self):
        # Test get_random_number with valid range
        min_value = 1
        max_value = 10
        random_number = get_random_number(min_value, max_value)
        self.assertGreaterEqual(random_number, min_value)
        self.assertLessEqual(random_number, max_value)

        # Test get_random_number with invalid range
        with self.assertRaises(ValueError):
            get_random_number(10, 1)

    def test_get_random_float(self):
        # Test get_random_float with valid range
        min_value = 1.0
        max_value = 10.0
        random_number = get_random_float(min_value, max_value)
        self.assertGreaterEqual(random_number, min_value)
        self.assertLessEqual(random_number, max_value)

        # Test get_random_float with invalid range
        with self.assertRaises(ValueError):
            get_random_float(10.0, 1.0)

if __name__ == "__main__":
    unittest.main(exit=False)
    main()