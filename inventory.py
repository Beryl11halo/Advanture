# inventory.py

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"You added {item} to your inventory.")

def add_item(inventory, item):
    inventory.add_item(item)
