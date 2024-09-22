# Coffee Vending Machine Documentation
## Table of Contents
1. Overview
2. Features
3. Class and Methods
    1. __init__()
    2. display_menu()
    3. get_valid_input()
    4. process_coins()
    5. is_transaction_successful()
    6. make_coffee()
    7. resource_check()
    8. display_status()
    9. run()
4. Resources Management
5. Transaction Handling
6. Future Improvements
### 1. Overview
This project implements a Coffee Vending Machine simulator that allows users to:

- Order various coffee drinks (Espresso, Latte, Cappuccino).
- Pay with coins (quarters, dimes, nickels, pennies).
- Check machine resources and track profits.

The machine manages resources (water, milk, coffee, cups) and calculates profits based on transactions. If resources are insufficient or the payment is not enough, the user is notified.

### 2. Features
+ Menu Display: Shows the available coffee drinks with their prices.
+ Coin Processing: Allows users to insert coins and calculate total payment.
+ Resource Management: Tracks and manages available water, milk, coffee, and cups.
+ Transaction Handling: Checks if the user has inserted enough money and provides change if necessary.
+ Dynamic Quantity: Allows ordering multiple cups of coffee at once.
+ Status Display: Shows current resource levels and total profit.
+ Exit with Confirmation: Confirms before exiting the machine.
### 3. Class and Methods
CoffeeMachine Class
The CoffeeMachine class defines the structure and functionality of the vending machine. Below are the details of its methods:

#### 1. __init__()
This is the constructor method that initializes the machine with:

A menu of drinks (Espresso, Latte, Cappuccino) with their respective costs and required ingredients.
Coin values for calculating the total payment.
Initial resource levels (water, milk, coffee, cups).
An initial profit of $0.0.
Example:

```python
machine = CoffeeMachine()  # Creates a new coffee machine instance.
```
#### 2. display_menu()
Displays the coffee menu with drink options and their prices.

Example:

```python
machine.display_menu()  # Outputs the menu to the console.
```
#### 3. get_valid_input()
A helper function that ensures the user provides valid integer input (used for coin entry and quantity selection). It keeps asking until a valid input is provided.

Example:

```python
quantity = machine.get_valid_input("Enter the quantity: ")  # Ensures valid number input.
```
#### 4. process_coins()
Calculates the total amount of money inserted by the user based on the number of quarters, dimes, nickels, and pennies. The value is returned in dollars.

Example:

```python
payment = machine.process_coins()  # Returns the total money inserted by the user.
```
#### 5. is_transaction_successful()
This method checks if the total amount of money inserted by the user is enough to cover the cost of the coffee(s). If not, it prompts the user to add more money.

Parameters:

payment: Total amount of money inserted.
cost: The cost of one cup of the selected drink.
quantity: Number of cups ordered.
Returns: The remaining change (if any) after the transaction.

Example:
```python
change = machine.is_transaction_successful(payment, cost, quantity)  # Calculates change or prompts for more coins.
```
#### 6. make_coffee()
This method deducts the ingredients and cups from the machine's resources and serves the coffee(s). It prints a confirmation message after preparing the order.

Parameters:

choice: The selected drink.
ingredients: The required ingredients for the chosen drink.
quantity: Number of cups ordered.
Example:

```python
machine.make_coffee("Latte", {"water": 200, "milk": 150, "coffee": 24}, 2)  # Prepares 2 cups of Latte.
```
#### 7. resource_check()
Checks if the machine has enough resources to prepare the selected drink in the specified quantity. It prints an error message if any resource is insufficient.

Parameters:

+ choice: The selected drink.
+ quantity: Number of cups ordered.

Returns: True if resources are sufficient, False otherwise.

Example:

```python
if machine.resource_check("Espresso", 1):
    # Proceed with the order
```
#### 8. display_status()
Displays the current levels of resources (water, milk, coffee, cups) and the total profit earned by the machine.

Example:

``` python
machine.display_status()  # Outputs the current resource status and profit.
```
#### 9. run()
The main loop of the coffee machine. It interacts with the user, allowing them to:

+ Order coffee.
+ Check the status of the machine.
+ Exit the program.

```python
machine.run()  # Starts the coffee machine interaction.
```

### Resources Management
+ Water: Measured in milliliters (ml).
+ Milk: Measured in milliliters (ml).
+ Coffee: Measured in grams (g).
+ Cups: Count of available cups.

These resources are consumed based on the drink ordered and the number of cups. The machine checks if there are enough resources before proceeding with the transaction.

### Transaction Handling
The machine calculates the total cost based on the drink and quantity. It processes coin input and ensures the payment is sufficient. If not, the user is prompted to insert more coins. After a successful transaction, change is returned to the user.

### Future Improvements
1. Card Payment System: Add support for credit/debit card transactions.
2. Inventory Refill Alerts: Add functionality to alert when resources are running low.
3. Admin Mode: Create an admin mode to easily refill resources or adjust prices.
4. Drink Customization: Allow customers to customize their drinks (e.g., extra coffee or milk).







