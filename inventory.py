class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def use_item(self, item):
        if item in self.items and self.items[item] > 0:
            self.items[item] -= 1
            return item
        print("Item not available.")
        return None
