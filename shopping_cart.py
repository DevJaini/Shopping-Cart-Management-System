# Importing "uuid" library to generate unique id.
import uuid
# Importing "re" library to support for regular expressions.
import re
# Importing "copy" library to support for shallow and deep copy operation.
import copy

# Now, creating "shoppingcart" class to manage adding, updating, and removing items, 
# calculating total cost and providing validation for input values.
class ShoppingCart:

    ITEM_NAME_MAX_LENGTH = 50
    CUSTOMER_ID_PATTERN = re.compile(r'^[A-Z]{3}\d{5}[A-Z]{2}[AQ]$')

    # Initialing a new shopping cart with a generating unique ID and assigning a customer ID.
    def __init__(self, customer_id):
        self._id = uuid.uuid4()
        self._customer_id = customer_id
        self._items = {}

    # Returns the ID of the shopping cart.
    @property
    def id(self):
        return str(self._id)

    # Returns the customer ID of the shopping cart.
    @property
    def customer_id(self):
        return self._customer_id

    # Returns a copy of the items in the shopping cart.
    @property
    def items(self):
        return copy.deepcopy(self._items)

    # Adds an item to the shopping cart.
    def add_item(self, item_name, quantity, price):
        # Verifying if the item name is too long, quantity is negative or zero, or price is negative.
        if len(item_name) > self.ITEM_NAME_MAX_LENGTH:
            raise ValueError("Item name exceeds maximum length")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if price < 0:
            raise ValueError("Price cannot be negative")
        self._items[item_name] = {'quantity': quantity, 'price': price}

    # Updates the quantity of an item in the shopping cart.
    def update_item_quantity(self, item_name, quantity):
        # Verifying if the quantity is negative or zero, or if the item is not in the cart.
        if item_name not in self._items:
            raise ValueError("Item not found in cart")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self._items[item_name]['quantity'] = quantity

    # Removes an item from the shopping cart.
    def remove_item(self, item_name):
        # Verifying if the item is not in the cart.
        if item_name not in self._items:
            raise ValueError("Item not found in cart")
        del self._items[item_name]

    # Calculates and returns the total cost of all items in the shopping cart.
    def get_total_cost(self):
        return sum(item['quantity'] * item['price'] for item in self._items.values())

    @staticmethod
    # Validating the value, name of the field and maximum length of the string
    def validate_string(value, field_name, max_length=None):
        # If the string is empty, exceeds the maximum length.
        if not value:
            raise ValueError(f"{field_name} cannot be empty")
        if max_length and len(value) > max_length:
            raise ValueError(f"{field_name} exceeds maximum length")

    @staticmethod
    # Validating the value and name of the field of the integer-
    def validate_integer(value, field_name):
        # If the value is not an integer or is negative.
        if not isinstance(value, int):
            raise ValueError(f"{field_name} must be an integer")
        if value < 0:
            raise ValueError(f"{field_name} must be non-negative")

    @staticmethod
    # Validating the value, regular expression and name of the field of the pattern
    def validate_pattern(value, pattern, field_name):
        # If the value does not match the pattern.
        if not pattern.match(value):
            raise ValueError(f"{field_name} does not match the required pattern")

# Unit tests - using the built-in "unittest" framework for writing and running unit tests. 
# unittest is a popular testing framework included in Python's standard library, 
# designed to support automated testing in Python code. 
# With unittest, we define test cases by creating classes that inherit from `unittest.TestCase`. 

import unittest

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart(customer_id="ABC12345DEQ")

    def test_cart_id_generation(self):
        self.assertIsInstance(uuid.UUID(self.cart.id), uuid.UUID)

    def test_customer_id_validation(self):
        self.assertTrue(ShoppingCart.CUSTOMER_ID_PATTERN.match(self.cart.customer_id))

    def test_add_item(self):
        self.cart.add_item("Product1", 2, 10.0)
        print("Added item:", self.cart.items)        
        self.assertEqual(self.cart.items["Product1"]["quantity"], 2)

    def test_update_item_quantity(self):
        self.cart.add_item("Product1", 2, 10.0)
        self.cart.update_item_quantity("Product1", 3)
        print("Items after update:", self.cart.items)
        self.assertEqual(self.cart.items["Product1"]["quantity"], 3)

    def test_remove_item(self):
        self.cart.add_item("Product1", 2, 10.0)
        self.cart.remove_item("Product1")
        print("Items after removal:", self.cart.items)
        self.assertNotIn("Product1", self.cart.items)

    def test_total_cost(self):
        self.cart.add_item("Product1", 2, 10.0)
        self.cart.add_item("Product2", 3, 15.0)
        total_cost = self.cart.get_total_cost()
        print("Total cost:", total_cost)
        self.assertEqual(self.cart.get_total_cost(), 2*10.0 + 3*15.0)

    def test_validate_string(self):
        with self.assertRaises(ValueError):
            ShoppingCart.validate_string("", "Test Field")
        with self.assertRaises(ValueError):
            ShoppingCart.validate_string("Too long string" * 100, "Test Field", max_length=20)

    def test_validate_integer(self):
        with self.assertRaises(ValueError):
            ShoppingCart.validate_integer(-5, "Test Field")
        with self.assertRaises(ValueError):
            ShoppingCart.validate_integer("not an integer", "Test Field")

    def test_validate_pattern(self):
        with self.assertRaises(ValueError):
            ShoppingCart.validate_pattern("invalid_customer_id", ShoppingCart.CUSTOMER_ID_PATTERN, "Customer ID")

# We then run the tests using the unittest.main() function, 
# which automatically discovers test cases and runs them.
if __name__ == '_main_':
    unittest.main()