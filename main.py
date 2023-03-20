"""
This is the main function that runs the automobile inventory program.

This function initializes the automobile inventory and starts an infinite loop where the user is prompted for a
selection from the menu. If the selection is valid, the corresponding action is performed on the inventory.
The program quits if the user selects 'Q' or an invalid selection is made.
"""

# Import modules
from menu_actions import get_user_selection, MENU_ACTIONS, ADD_SAMPLE_DATA, quit_program
from automobile_inventory import AutomobileInventory


def main():

    print("\n\t\t\tAutomobile Inventory Management System\n")
    inventory = AutomobileInventory()

    while True:
        selection = get_user_selection()
        if selection == 'Q':
            quit_program()

        if selection in MENU_ACTIONS:
            action = MENU_ACTIONS[selection]

            if action is not None:
                action(inventory)
            else:
                break
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()

