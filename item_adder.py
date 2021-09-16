from src.inbound import Truck, Inventory

def bill_of_lading() -> dict:
    items = {}
    while True:
        item = input("enter an item: ")
        qty = input("enter a quantity ")

        if not item:
            print(items)
            return items

        items[item] = qty

def truck_delivery(manifest):
    truck = Truck()
    truck.inventory = manifest 
    return truck

items = bill_of_lading()
truck_1 = truck_delivery(items)
print(truck_1.inventory)
