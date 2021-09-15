
def bill_of_lading() -> dict:
    items = {}
    while True:
        item = input("enter an item: ")
        qty = input("enter a quantity ")

        if not item:
            print(items)
            return items

        items[item] = qty

bill_of_lading()

