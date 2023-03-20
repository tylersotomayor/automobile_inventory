import json


class AutomobileInventory:
    def __init__(self):
        """
        Constructor for the AutomobileInventory class.
        Initializes an empty list to hold Automobile objects.
        """
        self.automobiles = []

    def add_auto(self, auto):
        """
        Adds an automobile to the inventory.
        Args:
            auto (Automobile): The automobile to add to the inventory.
        """
        self.automobiles.append(auto)

    def display_autos(self):
        """
        Displays the automobiles in the inventory.
        If the inventory is empty, prints a message saying so.
        """
        if self.automobiles:
            for automobile in self.automobiles:
                print(automobile)
        else:
            print("No automobiles in inventory.")

    def get_stats(self):
        """
       Prints statistics about the automobiles in the inventory.
       If the inventory is empty, prints a message saying so.
       """
        total_automobiles = len(self.automobiles)
        if total_automobiles == 0:
            print("No automobiles in inventory.")
            return

        max_price = max(self.automobiles, key=lambda x: x.get_price())
        min_price = min(self.automobiles, key=lambda x: x.get_price())
        avg_price = sum([auto.get_price() for auto in self.automobiles]) / total_automobiles

        print(f"Number of automobiles: {total_automobiles}")
        print(f"Most expensive automobile: \n\t{max_price}")
        print(f"Least expensive automobile: \n\t{min_price}")
        print(f"Average price of an automobile: \n\t${avg_price:,.2f}")

    def save_data(self):
        """
        Saves the current inventory of automobiles to a JSON file.
        """
        with open(self.filename, "w") as f:
            json.dump([auto.__dict__ for auto in self.automobiles], f, indent=4)

    def load_data(self):
        """
        Loads the inventory of automobiles from a JSON file.
        If the file does not exist, does nothing.
        """
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.automobiles = [Automobile(**auto_data) for auto_data in data]
        except FileNotFoundError:
            pass

    def clear_data(self):
        """
        Clears the inventory of automobiles and saves the changes to the JSON file.
        """
        self.automobiles = []
        self.save_data()

