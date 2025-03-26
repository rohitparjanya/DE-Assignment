Random Number Generator App
============================
### Overview

The Random Number Generator App is a Python-based application that generates random integers and floating-point numbers within user-specified ranges. The app provides a simple menu-driven interface for users to select the type of random number they want to generate.

### Installation Instructions

To use the Random Number Generator App, follow these steps:

1. **Install Python**: Ensure you have Python installed on your system. You can download the latest version from the [official Python website](https://www.python.org/downloads/).
2. **Save the Code**: Save the provided Python code in a file with a `.py` extension, for example, `random_number_generator.py`.
3. **Run the App**: Open a terminal or command prompt, navigate to the directory where you saved the file, and run the app using the command `python random_number_generator.py`.

### Usage Examples

Here are some examples of how to use the Random Number Generator App:

* **Generate a Random Integer**:
	1. Run the app and select option 1 from the menu.
	2. Enter the minimum and maximum values for the random integer range.
	3. The app will display a random integer within the specified range.
* **Generate a Random Float**:
	1. Run the app and select option 2 from the menu.
	2. Enter the minimum and maximum values for the random float range.
	3. The app will display a random floating-point number within the specified range.

### API Reference

The Random Number Generator App provides the following functions:

#### `get_input(prompt: str, input_type: type, max_attempts: int = MAX_ATTEMPTS) -> input_type`

* **Description**: Gets user input and attempts to convert it to the specified type.
* **Parameters**:
	+ `prompt`: The prompt to display to the user.
	+ `input_type`: The type to which the input should be converted.
	+ `max_attempts`: The maximum number of attempts to get a valid input (default: `MAX_ATTEMPTS`).
* **Returns**: The user's input as the specified type.
* **Raises**: `ValueError` if the input cannot be converted to the specified type after `max_attempts`.

#### `get_random_number(min_value: int, max_value: int) -> int`

* **Description**: Generates a random integer between `min_value` and `max_value` (inclusive).
* **Parameters**:
	+ `min_value`: The minimum value for the random number.
	+ `max_value`: The maximum value for the random number.
* **Returns**: A random integer between `min_value` and `max_value`.

#### `get_random_float(min_value: float, max_value: float) -> float`

* **Description**: Generates a random floating-point number between `min_value` and `max_value`.
* **Parameters**:
	+ `min_value`: The minimum value for the random number.
	+ `max_value`: The maximum value for the random number.
* **Returns**: A random floating-point number between `min_value` and `max_value`.
* **Raises**: `ValueError` if `min_value` is greater than `max_value`.

#### `display_menu() -> None`

* **Description**: Displays the menu for the Random Number Generator App.
* **Parameters**: None
* **Returns**: None

#### `generate_random_integer() -> None`

* **Description**: Generates a random integer within a user-specified range.
* **Parameters**: None
* **Returns**: None

#### `generate_random_float() -> None`

* **Description**: Generates a random floating-point number within a user-specified range.
* **Parameters**: None
* **Returns**: None

#### `main() -> None`

* **Description**: The main function for the Random Number Generator App.
* **Parameters**: None
* **Returns**: None

### Unit Tests

The Random Number Generator App includes unit tests to ensure the functions work as expected. You can run the tests using the `unittest` module.

### Troubleshooting

If you encounter any issues while using the Random Number Generator App, check the following:

* Ensure you have Python installed and the code is saved in a file with a `.py` extension.
* Verify that you are running the app from the correct directory.
* Check the input values for the random number range to ensure they are valid.

By following these instructions and using the Random Number Generator App, you can generate random integers and floating-point numbers within user-specified ranges.