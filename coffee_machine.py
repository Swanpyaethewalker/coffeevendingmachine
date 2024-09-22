# Define the Coffee Vending Machine class
class CoffeeMachine:
    def __init__(self):
        # Initialize the menu with drink options, costs, and ingredient requirements
        self.MENU = {
            "Espresso": {
                "cost": 1.50,
                "ingredients": {"water": 50, "coffee": 18}
            },
            "Latte": {
                "cost": 2.50,
                "ingredients": {"water": 200, "milk": 150, "coffee": 24}
            },
            "Cappuccino": {
                "cost": 3.00,
                "ingredients": {"water": 250, "milk": 100, "coffee": 24}
            }
        }
        
        # Define coin values in cents
        self.COIN_VALUES = {
            "quarter": 25,
            "dime": 10,
            "nickel": 5,
            "penny": 1
        }
        
        # Set initial resource levels (in milliliters for liquids and count for cups)
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "cups": 10
        }
        
        # Initialize profit to 0.0
        self.profit = 0.0

    # Display the menu of drinks and their prices
    def display_menu(self):
        print("Menu:")
        for drink, details in self.MENU.items():
            print(f"{drink}: ${details['cost']}")

    # Helper function to get valid integer input (prevents non-numeric input errors)
    def get_valid_input(self, prompt):
        while True:
            try:
                value = int(input(prompt))  # Try converting input to integer
                return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")  # Handle invalid input

    # Process the user's coin input and calculate the total amount in dollars
    def process_coins(self):
        total_amount = 0

        # Use helper function to validate and get the number of each type of coin
        num_quarters = self.get_valid_input("Enter number of quarters: ")
        total_amount += num_quarters * self.COIN_VALUES["quarter"]

        num_dimes = self.get_valid_input("Enter number of dimes: ")
        total_amount += num_dimes * self.COIN_VALUES["dime"]

        num_nickels = self.get_valid_input("Enter number of nickels: ")
        total_amount += num_nickels * self.COIN_VALUES["nickel"]

        num_pennies = self.get_valid_input("Enter number of pennies: ")
        total_amount += num_pennies * self.COIN_VALUES["penny"]

        # Return the total amount in dollars (convert cents to dollars)
        return total_amount / 100

    # Check if the transaction is successful based on the payment and cost
    def is_transaction_successful(self, payment, cost, quantity):
        total_cost = cost * quantity  # Calculate the total cost for multiple cups
        # Continue asking for more coins if payment is insufficient
        while payment < total_cost:
            print(f"Sorry, you only entered ${payment:.2f}, which is not enough for ${total_cost:.2f}.")
            additional_payment = self.process_coins()  # Allow user to add more coins
            payment += additional_payment
        
        # Add the cost to the machine's profit
        self.profit += total_cost
        # Return the remaining change to the customer
        return payment - total_cost

    # Deduct the ingredients from resources and serve the coffee
    def make_coffee(self, choice, ingredients, quantity):
        for ingredient, amount in ingredients.items():
            # Deduct the required quantity of each ingredient from the resources
            self.resources[ingredient] -= amount * quantity
        # Deduct the required number of cups
        self.resources["cups"] -= quantity
        
        # Serve the coffee
        print(f"Here is your {quantity} cup(s) of {choice}. Enjoy!")

    # Check if there are enough resources to fulfill the order
    def resource_check(self, choice, quantity):
        ingredients = self.MENU[choice]["ingredients"]  # Get the ingredients for the selected drink
        for ingredient, amount in ingredients.items():
            # If any ingredient is insufficient, return False
            if self.resources[ingredient] < amount * quantity:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        # Check if there are enough cups
        if self.resources["cups"] < quantity:
            print("Sorry, there are not enough cups.")
            return False
        
        # If all resources are sufficient, return True
        return True

    # Display the current resource levels and total profit
    def display_status(self):
        print("Resources:")
        for ingredient, amount in self.resources.items():
            # Display water, milk, and coffee in milliliters, and cups as counts
            print(f"{ingredient.capitalize()}: {amount}ml" if ingredient != "cups" else f"{ingredient.capitalize()}: {amount} cups")
        # Display the total profit earned
        print(f"Profit: ${self.profit:.2f}")

    # Main function to run the coffee machine
    def run(self):
        # Continuously prompt the user for actions until 'exit' is selected
        while True:
            action = input("What would you like to do? (order/status/exit): ").lower()
            
            # Handle 'order' action
            if action == "order":
                self.display_menu()  # Show the drink menu
                choice = input("Enter the drink you want to order: ").capitalize()  # Get user's drink choice
                if choice in self.MENU:
                    # Get the quantity and check if enough resources are available
                    quantity = self.get_valid_input("Enter the quantity: ")
                    if self.resource_check(choice, quantity):
                        cost = self.MENU[choice]["cost"]  # Get the cost of the chosen drink
                        payment = self.process_coins()  # Process coin input from the user
                        change = self.is_transaction_successful(payment, cost, quantity)  # Check transaction success
                        if change is not None:
                            self.make_coffee(choice, self.MENU[choice]["ingredients"], quantity)  # Make the coffee
                            if change > 0:
                                # Return any change to the customer
                                print(f"Here is ${change:.2f} in change.")
                else:
                    # Handle invalid drink choice
                    print("Invalid choice. Please select a valid drink.")
            
            # Handle 'status' action to show the current status of resources and profit
            elif action == "status":
                self.display_status()
            
            # Handle 'exit' action to turn off the machine with confirmation
            elif action == "exit":
                confirm = input("Are you sure you want to exit? (yes/no): ").lower()
                if confirm == "yes":
                    print("Turning off the coffee machine. Goodbye!")
                    break
            
            # Handle invalid actions
            else:
                print("Invalid action. Please choose 'order', 'status', or 'exit'.")

# Create an instance of CoffeeMachine and run the program
machine = CoffeeMachine()
machine.run()
