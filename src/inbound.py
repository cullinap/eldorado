

class Truck:

    def __init__(self, inventory):
        self.inventory = inventory

    def display_inventory(self):
        for item in self.inventory:
            print(item)
