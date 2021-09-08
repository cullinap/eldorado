

class Truck:

    def __init__(self):
        self.inventory = None
        self.nextShipment = None

    def display_inventory(self):
        for item in self.inventory:
            print(item)

class Inventory:

    def __init__(self):
        self.head = Truck()
    
    def addShipment(self, data):
        new_node = data
        cur = self.head
        while cur.nextShipment != None:
            cur = cur.nextShipment
        cur.nextShipment = new_node

    def display(self):
        shipments = []
        cur = self.head
        while cur.nextShipment != None:
            cur = cur.nextShipment
            print(cur.inventory)

