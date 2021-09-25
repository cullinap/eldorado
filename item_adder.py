from src.inbound import Truck, Inventory
from src.minimalBlock import MinimalBlock, ItemBlock, AccessoryBlock
import json

def bill_of_lading() -> dict:
    items = {}
    while True:
        item = input("enter an item: ")
        qty = input("enter a quantity ")

        if not item:
            print(f'this is in the fn {items}')
            return items

        items[item] = qty

def truck_delivery(manifest):
    truck = Truck()
    truck.inventory = manifest 
    return truck

def bill_of_lading_json(contents: dict) -> json:
    return json.dumps(contents)

def store_items_in_db(shipment):
    # conceptually store items in from this function once postgres up
    add_item_to_db = shipment
    return add_item_to_db

items = bill_of_lading()
truck_1 = truck_delivery(items)
truck_json = bill_of_lading_json(truck_1.inventory)
initial_block = ItemBlock("Initial String", [truck_json])
add_to_db = store_items_in_db(initial_block)
print(initial_block.block_hash, initial_block.block_data)
print(truck_1.inventory)


