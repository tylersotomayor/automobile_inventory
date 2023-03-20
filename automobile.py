class Automobile:
    """
    A class to represent an automobile.
    """

    def __init__(self, vin, make, model, year, price):
        """
        Initialize the Automobile object with the given attributes.
        """
        self.set_vin(vin)
        self.set_make(make)
        self.set_model(model)
        self.set_year(year)
        self.set_price(price)

    def __str__(self):
        """
        Return a formatted string representation of the Automobile object.
        """
        return f"VIN: {self.vin:<17}  Make: {self.make:<15}  Model: {self.model:<18} Year: {self.year:<5}  " \
               f"Price: ${self.price:>10,.2f} "

    # Getter methods
    def get_vin(self):
        """
        Return the vehicle identification number (VIN) of the automobile.
        """
        return self.vin

    def get_make(self):
        """
        Return the make of the automobile.
        """
        return self.make

    def get_model(self):
        """
        Return the model of the automobile.
        """
        return self.model

    def get_year(self):
        """
        Return the year of the automobile.
        """
        return self.year

    def get_price(self):
        """
        Return the price of the automobile.
        """
        return self.price

    # Setter methods

    def set_vin(self, vin):
        """
        Set the vehicle identification number (VIN) of the automobile.
        Validate the input and raise an error if it's not valid.
        """
        if not isinstance(vin, str) or len(vin) != 17 or not vin.isalnum():
            raise ValueError(
                "Invalid Vehicle Identification Number. VIN must be a 17 character alphanumeric string.")
        self.vin = vin.upper()

    def set_make(self, make):
        """
        Set the make of the automobile.
        Validate the input and raise an error if it's not valid.
        Stores the make in sentence case
        """
        if not isinstance(make, str):
            raise ValueError("Invalid make. Vehicle make must be a string.")
        self.make = make.title()

    def set_model(self, model):
        """
        Set the model of the automobile.
        Validate the input and raise an error if it's not valid.
        Stores the model in sentence case
        """
        if not isinstance(model, str):
            raise ValueError("Invalid model. Vehicle model must be a string.")
        self.model = model.title()

    def set_year(self, year):
        """
        Set the year of the automobile.
        Validate the input and raise an error if it's not valid.
        """
        if not isinstance(year, int) or year < 1900 or year > 2024:
            raise ValueError("Invalid year. Year must be an integer between 1900 and 2024.")
        self.year = year

    def set_price(self, price):
        """
        Set the price of the automobile.
        Validate the input and raise an error if it's not valid.
        """
        if not isinstance(price, float) or price > 200000:
            raise ValueError("Invalid price. Price must be a float less than or equal to 200,000.")
        self.price = price

