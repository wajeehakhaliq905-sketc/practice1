class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(f"No item named {name}")
        del self.items[name]

    def total_value(self):
        return sum(qty * price for qty, price in self.items.values())

    def __len__(self):
        return len(self.items)


inventory = Inventory()

with open("stock.txt", "r") as file:
    for line in file:
        try:
            name, qty, price = line.strip().split(",")
            qty = int(qty)
            price = float(price)
            inventory.add_item(name, qty, price)

        except ValueError:
            print("Skipping bag: bad number")

print(len(inventory), "Item ", "Total value:", inventory.total_value())
inventory.remove_item("pen")
# After removing pen
print( len(inventory), "Item ", "Total value:", inventory.total_value())

try:
    inventory.remove_item("laptop")
except KeyError as e:
    print("Error:",e)










'''class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def total_value(self):
        return sum(qty * price for qty, price in self.items.values())

    def save_report(self, filename):
        with open(filename, "w") as file:
            for name, (qty, price) in self.items.items():
                file.write(f"{name}: quantity={qty}, price={price}\n")

            file.write(f"Total value: {self.total_value()}\n")


inventory = Inventory()
inventory.add_item("pen", 10, 25)
inventory.add_item("notebook", 5, 120)
inventory.add_item("marker", 4, 80)

inventory.save_report("report.txt")
print("Report saved successfully!")'''