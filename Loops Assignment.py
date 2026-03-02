# Taco Palace Ordering System

# Function to print the menu
def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco - $2.50")
    print("2. Burrito - $5.00")
    print("3. Nachos - $4.25")
    print("4. Soft Drink - $1.75")
    print("5. Quit")


# Function to get price based on selection
def get_price(selection):
    if selection == 1:
        return 2.50
    elif selection == 2:
        return 5.00
    elif selection == 3:
        return 4.25
    elif selection == 4:
        return 1.75
    else:
        return 0


# Function to get item name based on selection
def get_item_name(selection):
    if selection == 1:
        return "Taco"
    elif selection == 2:
        return "Burrito"
    elif selection == 3:
        return "Nachos"
    elif selection == 4:
        return "Soft Drink"
    else:
        return ""


# Main Program
def main():
    total = 0
    order_list = []

    print("Welcome to Taco Palace! Please view the menu below and enter the number that represents your selection.")

    while True:
        print_menu()

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1-5.")
            continue

        if choice == 5:
            break
        elif 1 <= choice <= 4:
            item = get_item_name(choice)
            price = get_price(choice)

            print(f"You selected a {item}")

            order_list.append(item)
            total += price
        else:
            print("Invalid choice. Please select a number from 1-5.")

    # Final Output
    if len(order_list) > 0:
        print("\nYou ordered:", ", ".join(order_list))
        print(f"Your total is ${total:.2f}")
    else:
        print("\nYou did not order anything.")


# Run the program
main()