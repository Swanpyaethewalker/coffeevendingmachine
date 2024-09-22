import unittest
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from coffee_machine import CoffeeMachine

class TestCoffeeMachine(unittest.TestCase):

    def setUp(self):
        """Set up a CoffeeMachine instance for testing."""
        self.machine = CoffeeMachine()

    def test_initial_resources(self):
        """Test initial resource levels."""
        self.assertEqual(self.machine.resources['water'], 300)
        self.assertEqual(self.machine.resources['milk'], 200)
        self.assertEqual(self.machine.resources['coffee'], 100)
        self.assertEqual(self.machine.resources['cups'], 10)

    def test_resource_check_sufficient(self):
        """Test resource check for a drink that has enough resources."""
        self.assertTrue(self.machine.resource_check('Latte'))

    def test_resource_check_insufficient(self):
        """Test resource check for a drink with insufficient resources."""
        self.machine.resources['milk'] = 0  # Set milk to 0
        self.assertFalse(self.machine.resource_check('Latte'))

    def test_successful_transaction(self):
        """Test a successful transaction."""
        payment = 3.00  # Enough for a Latte
        cost = self.machine.MENU['Latte']['cost']
        change = self.machine.is_transaction_successful(payment, cost, 1)
        self.assertEqual(change, payment - cost)
        self.assertEqual(self.machine.profit, cost)

    def test_unsuccessful_transaction(self):
        """Test an unsuccessful transaction due to insufficient payment."""
        payment = 1.00  # Not enough for a Latte
        cost = self.machine.MENU['Latte']['cost']
        change = self.machine.is_transaction_successful(payment, cost, 1)
        self.assertIsNone(change)
        self.assertEqual(self.machine.profit, 0)

    def test_make_coffee(self):
        """Test making coffee updates resources correctly."""
        self.machine.make_coffee('Espresso', self.machine.MENU['Espresso']['ingredients'], 1)
        self.assertEqual(self.machine.resources['water'], 250)  # 300 - 50
        self.assertEqual(self.machine.resources['coffee'], 82)   # 100 - 18
        self.assertEqual(self.machine.resources['cups'], 9)      # 10 - 1

if __name__ == '__main__':
    unittest.main()
