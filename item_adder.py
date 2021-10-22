from src.inbound import Truck, Inventory
from src.minimalBlock import MinimalBlock, ItemBlock, AccessoryBlock
from src.inventory_report import print_inventory
import json
import sqlite3

def bill_of_lading() -> dict:
    items = {}
    while True:
        item = input("enter an item: ")
        qty = input("enter a quantity ")

        if not item:
            return items

        items[item] = int(qty)

def truck_delivery(manifest):
    truck = Truck()
    truck.inventory = manifest 
    return truck

def bill_of_lading_json(contents: dict) -> json:
    return json.dumps(contents)

def store_items_in_db(shipment):
    conn = sqlite3.connect('database/warehouse.sqlite')
    cur = conn.cursor()
    
    table_schema = """
    CREATE TABLE IF NOT EXISTS inventory ( 
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description INTEGER
    );
    """

    cur.execute(table_schema)
  
    item = list(shipment.keys())[0] 
    value = shipment[item]

    item_list = list(shipment.keys())

    # make sure ? does not have quotes otherwise binding error
    insert_query = """
    INSERT INTO inventory (name, description)
    VALUES (?, ?);
    """
    
    for i in item_list:
        cur.execute(insert_query, (str(i), shipment[i]))
        conn.commit()
    
    cur.execute('SELECT * FROM inventory')

    result = cur.fetchall()
    #print(result)
    
    cur.close()
    conn.close()


items = bill_of_lading()
truck_1 = truck_delivery(items)
truck_json = bill_of_lading_json(truck_1.inventory)
initial_block = ItemBlock("Initial String", [truck_json])

store_items_in_db(items)
print_inventory()
#print(initial_block.block_hash, initial_block.block_data)
#print(truck_1.inventory)
#print(add_to_db)


