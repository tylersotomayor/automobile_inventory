import json
import os

from automobile import Automobile
from automobile_inventory import AutomobileInventory
from sample_data import generate_random_autos

# Define menu selection constants
ADD_AUTO = 'A'
ADD_SAMPLE_DATA = 'G'
DISPLAY_AUTOS = 'D'
STATS = 'S'
SAVE_DATA = 'P'
LOAD_DATA = 'L'
CLEAR_DATA = 'C'
QUIT = 'Q'


def get_user_selection():
    while True:
        print("\nMain Menu")
        print(f"[{ADD_AUTO}]dd another automobile")
        print(f"[{DISPLAY_AUTOS}]isplay all automobiles")
        print(f"[{STATS}]tats about automobiles")
        print(f"[{ADD_SAMPLE_DATA}]enerate and add sample data")
        print(f"[{SAVE_DATA}]reserve data to file")
        print(f"[{LOAD_DATA}]oad data from file")
        print(f"[{CLEAR_DATA}]lear all data")
        print(f"[{QUIT}]uit")
        selection = input("\nEnter [selection]: ").upper()

        if selection in MENU_ACTIONS:
            return selection
        else:
            print("Invalid selection. Please try again.")


def add_auto(inventory):
    """
   Prompts the user to enter information about a new automobile, creates an Automobile object from the input,
   and adds it to the inventory.
   Args:
       inventory (AutomobileInventory): The inventory to which the automobile will be added.
   """
    while True:
        try:
            vin = input("Enter VIN: ")
            auto = Automobile(vin, "Placeholder", "Placeholder", 1900, 0.0)
            break
        except ValueError as e:
            print(e)

    make = input("Enter make: ")
    model = input("Enter model: ")

    while True:
        try:
            year = int(input("Enter year: "))
            auto.set_year(year)
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            price = float(input("Enter price: $"))
            auto.set_price(price)
            break
        except ValueError as e:
            print(e)

    auto.set_make(make)
    auto.set_model(model)

    # Prompt the user to confirm the input values
    print(f"\nYou entered the following information for the new automobile:")
    print(auto)
    confirmation = input("Do you want to add this automobile to the inventory? (Y/N): ").upper()
    if confirmation == "Y":
        inventory.add_auto(auto)
        print("Automobile added to inventory.")
    else:
        print("Automobile not added to inventory.")


def add_sample_data(inventory):
    """
    Generates a specified number of random automobiles and adds them to the inventory.

    Args:
        inventory (AutomobileInventory): The inventory to which the automobiles will be added.
    """
    while True:
        try:
            num_autos = int(input("Enter the number of sample automobiles to generate: "))
            break
        except ValueError as e:
            print(f"Invalid input. Please enter an integer. \n\t\tError: {e}")
    autos_data = generate_random_autos(num_autos)
    for auto_data in autos_data:
        try:
            auto = Automobile(auto_data["vin"], auto_data["make"], auto_data["model"], auto_data["year"],
                              auto_data["price"])
            inventory.add_auto(auto)
            print(f"Added {auto_data['make']} {auto_data['model']} to the inventory.")
        except ValueError as e:
            print(e)


def display_autos(inventory):
    """Displays all automobiles in the inventory."""
    inventory.display_autos()


def show_stats(inventory):
    """
    Displays various statistics about the automobiles in the inventory.
    """
    inventory.get_stats()


def save_data(inventory):
    """
    Save the inventory data to a JSON file.
    """
    with open("autos.json", "w") as f:
        data = {"autos": [vars(auto) for auto in inventory.automobiles]}
        json.dump(data, f, indent=4)
    print("Data saved successfully.")


def load_data(inventory):
    """
    Load inventory data from a JSON file.
    """
    if not os.path.exists("autos.json"):
        print("Data file not found.")
        return

    with open("autos.json", "r") as f:
        data = json.load(f)

    inventory.automobiles.clear()
    for auto_data in data["autos"]:
        auto = Automobile(**auto_data)
        inventory.add_auto(auto)

    print("Data loaded successfully.")


def clear_data(inventory):
    """
    Clear all data from the inventory.
    """
    inventory.automobiles.clear()
    print("Data cleared successfully.")


def quit_program():
    """
    Quits the program.
    """
    print("Goodbye!")
    raise SystemExit


# Dictionary to map menu selections to their corresponding functions.
MENU_ACTIONS = {
    ADD_AUTO: add_auto,
    DISPLAY_AUTOS: display_autos,
    STATS: show_stats,
    ADD_SAMPLE_DATA: add_sample_data,
    SAVE_DATA: save_data,
    LOAD_DATA: load_data,
    CLEAR_DATA: clear_data,
    QUIT: quit_program
}

