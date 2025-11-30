class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def setQuantity(self, quantity):
        self.quantity = quantity

    def calculateTotalValue(self):
        return self.price * self.quantity

    def calculate_total_inventory_value(self, products):
        return sum(product.calculateTotalValue() for product in products)
