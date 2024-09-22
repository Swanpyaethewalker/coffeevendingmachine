

# Coffee Vending Machine Project

## Project Overview

The Coffee Vending Machine is a Python-based simulation that allows users to order coffee drinks like Espresso, Latte, and Cappuccino. The program manages resources (water, milk, coffee, and cups) and tracks profits based on user transactions. The machine accepts payments in coins and returns change if necessary.

This project can be extended to include more features, such as a card payment system, more drink options, and additional resources. It's designed for both learning and practical use in understanding object-oriented programming (OOP), resource management, and basic user interactions in Python.

## Key Features:

+ Menu Display: Users can view available drinks and their prices.
+ Coin Payment: Users insert coins (quarters, dimes, nickels, pennies) to pay for their orders.
+ Resource Management: The machine tracks and manages resources like water, milk, coffee, and cups.
+ Profit Calculation: The machine keeps track of the total profit from transactions.
+ Multiple Orders: Users can order multiple cups of coffee at once.
+ Status Display: Displays current resource levels and profit.
+ Exit Option: Users can turn off the machine by exiting the program.
## Setup Instructions
### Prerequisites
+ Python: This project requires Python 3.x to run. You can download Python from the official Python website.
### Installation Steps
1. Clone the Repository If you have Git installed, you can clone the project repository using the following command:

```bash
git clone https://github.com/yourusername/coffee-vending-machine.git
```
Alternatively, you can download the project as a ZIP file and extract it.

2. Navigate to the Project Directory

```bash
cd coffee-vending-machine
```
3. Install Dependencies 
If there are any dependencies listed in a requirements.txt file (none in this project), install them using:

```bash
pip install -r requirements.txt
```
This project doesn't have any external dependencies at the moment, so you can skip this step if no requirements.txt is provided.

4. Run the Program Run the coffee_machine.py file to start the vending machine simulation:

```bash
python coffee_machine.py
```
5. Interact with the Machine

+ Choose a drink from the menu.
+ Insert coins to pay.
+ Get your coffee or check the machine's resources.
+ You can exit the program anytime by selecting the exit option.
### Running Tests (Optional)
If you have unit tests included in the tests/ folder, you can run them using pytest or the Python unittest framework:

1. Install pytest (if needed):

```bash
pip install pytest
```
2. Run the Tests:

```bash
pytest tests/
```
### Troubleshooting
+ Ensure you have the correct version of Python installed.
+ If you encounter any errors, verify the correct directory is being used when running the program.
+ You may need to install any additional dependencies if the program grows in complexity.

### License
This project is licensed under the MIT License. See the **LICENSE** file for details.

### Contribution
Feel free to fork this repository and submit pull requests. Contributions and suggestions are always welcome!