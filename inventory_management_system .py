import json


class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.product_id} | {self.name} | ₹{self.price} | Qty:{self.quantity}"

class InventoryManager:

    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def display_product(self):
        for product in self.inventory:
            print(product)

    def remove_product(self, product_id):
        for product in self.inventory:
            if product.product_id == product_id:
                self.inventory.remove(product)
                print("Item removed.")
                return True

        print("Item doesn't exist.")
        return False

    def sell_product(self, product_id):
        for product in self.inventory:
            if product.product_id == product_id:
                if product.quantity > 0:
                    product.quantity -= 1
                    print("Product sold.")
                    return True
                else:
                    print("Out of stock.")
                    return False

        print("Product not found.")
        return False

    def restock_product(self, product_id, quantity):
        for product in self.inventory:
            if product.product_id == product_id:
                product.quantity += quantity
                print("Stock updated.")
                return True

        print("Product not found.")
        return False

    def save_data(self):
        with open("inventory.json", "w") as file:

            data = [product.__dict__ for product in self.inventory]

            json.dump(data, file, indent=4)

        print("Inventory saved successfully.")

    def load_data(self):
        try:
            with open("inventory.json", "r") as file:

                data = json.load(file)

                self.inventory = []

                for product_data in data:
                    product = Product(**product_data)
                    self.inventory.append(product)

            print("Inventory loaded successfully.")

        except FileNotFoundError:
            print("No inventory file found. Starting with empty inventory.")



manager = InventoryManager()

manager.load_data()

if len(manager.inventory) == 0:

    manager.add_product(Product(101, "TV", 20000, 5))
    manager.add_product(Product(102, "Laptop", 50000, 3))

manager.restock_product(101, 10)
manager.sell_product(102)

manager.display_product()

manager.save_data()
