class Beverage:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.quantity} available)"

class VendingMachine:
    def __init__(self):
        self.inventory = {} # Use a dictionary to store beverages, e.g., {"Coke": Beverage(...)}
        self.current_balance = 0.0

    def add_beverage(self, beverage):
        self.inventory[beverage.name] = beverage

    def display_menu(self):
        print("\n--- Vending Machine Menu ---")
        for name, beverage in self.inventory.items():
            print(beverage)
        print("--------------------------")

    def select_item(self, item_name):
        if item_name in self.inventory:
            selected_beverage = self.inventory[item_name]
            if selected_beverage.quantity > 0:
                return selected_beverage
            else:
                print("Sorry, that item is out of stock.")
                return None
        else:
            print("Invalid selection. Please choose from the menu.")
            return None

    def insert_money(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Current balance: ${self.current_balance:.2f}")
        else:
            print("Please insert a positive amount of money.")

    def vend(self, item_name):
        selected_beverage = self.select_item(item_name)
        if selected_beverage:
            if self.current_balance >= selected_beverage.price:
                change = self.current_balance - selected_beverage.price
                selected_beverage.quantity -= 1
                self.current_balance = 0 # Reset balance after successful transaction
                print(f"Vending {selected_beverage.name}...")
                if change > 0:
                    print(f"Your change is ${change:.2f}")
                return True
            else:
                print(f"Insufficient funds. Please insert ${selected_beverage.price - self.current_balance:.2f} more.")
                return False
        return False

# --- Main Program ---
if __name__ == "__main__":
    machine = VendingMachine()
    # Add 6 beverages (example)
    machine.add_beverage(Beverage("Coke", 1.50, 10))
    machine.add_beverage(Beverage("Pepsi", 1.50, 8))
    machine.add_beverage(Beverage("Water", 1.00, 15))
    machine.add_beverage(Beverage("Sprite", 1.50, 7))
    machine.add_beverage(Beverage("Juice", 2.00, 5))
    machine.add_beverage(Beverage("Tea", 1.75, 9))

    while True:
        machine.display_menu()
        user_input = input("Enter beverage name to purchase, or 'quit' to exit: ").strip()

        if user_input.lower() == 'quit':
            break

        selected_item = machine.select_item(user_input)

        if selected_item:
            while True: # Loop for inserting money
                try:
                    money_str = input(f"Please insert money (or type 'cancel' to go back): $").strip()
                    if money_str.lower() == 'cancel':
                        break # Go back to beverage selection
                    amount_inserted = float(money_str)
                    machine.insert_money(amount_inserted)
                    if machine.vend(user_input): # Attempt to vend after inserting money
                        break # Successful vend, break money loop
                except ValueError:
                    print("Invalid input. Please enter a number for money or 'cancel'.")
        # else: (handled by select_item printing error message)

    print("Thank you for using the vending machine!")