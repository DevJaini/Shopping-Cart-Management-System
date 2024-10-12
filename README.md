# Shopping Cart Management System

This project is a Python implementation of a simple Shopping Cart Management System that supports adding, updating, and removing items, calculating total costs, and validating customer IDs and input fields. The system also provides a basic validation structure for inputs like customer ID patterns, string length, and integers. The project includes unit tests to ensure functionality and reliability.

## Features

	• Unique Shopping Cart ID: Automatically generates a unique ID for each shopping cart instance.
	• Customer ID Validation: Supports pattern matching for customer IDs (AAA12345BBQ format).
	• Item Management: Add, update, and remove items in the shopping cart.
	• Total Cost Calculation: Calculates the total cost of items in the cart.
	• Input Validation: Ensures proper input values such as non-negative quantities, prices, and string length checks.

## Project Structure

	• shoppingcart.py: Main Python file containing the ShoppingCart class and logic for managing items in the cart.
	• test_shoppingcart.py: Python file for testing the functionality using the unittest module.

## Libraries Used

	• uuid: For generating unique IDs for the shopping cart.
	• re: For handling regular expressions (used for validating customer IDs).
	• copy: To provide deep copy functionality for the shopping cart items.
	• unittest: For creating unit tests to validate the shopping cart functionalities.

## Installation

To get started, you need to have Python installed on your machine.

1. Clone the repository:

```bash
git clone https://github.com/yourusername/shopping-cart.git
cd shopping-cart
```

## Running Tests

To run the unit tests, use the following command:

```bash
python -m unittest discover
```

The test cases are located in the test_shoppingcart.py file and will ensure that the shopping cart behaves as expected.

Test Cases

	• ID Generation: Validates that each shopping cart has a unique UUID.
	• Customer ID Validation: Ensures the customer ID follows the specified pattern.
	• Add, Update, Remove Items: Tests adding, updating, and removing items from the cart.
	• Total Cost Calculation: Verifies the correct total cost is calculated.
	• Input Validation: Ensures input values (string lengths, integers, patterns) are correctly validated.
