from product import Product

# Storage for the products
products = []


def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    new_product = Product(name, price, quantity)
    products.append(new_product)

    print(f"Product '{new_product.getName()}' added successfully.")


def updateQuantity():
    name = input("Enter Product Name to Update:")

    for product in products:
        if product.getName() == name:
            new_quantity = int(input("Enter New Quantity: "))
            product.setQuantity(new_quantity)
            print(
                f"Quantity for '{product.getName()}' updated to {new_quantity}.")
            return
    print(f"Product '{name}' not found.")


def displayInventory():

    if not products:
        print("No products in inventory.")
        return

    print("\nCurrent Inventory:")
    print(f"{'Name':<25}{'Price':<25}{'Quantity':<25}{'Total Value':<25}")

    for product in products:
        total_value = product.calculateTotalValue()
        print(f"{product.getName():<25}{product.getPrice():<25}{product.getQuantity():<25}${total_value:<25.2f}")
        overall_value = product.calculate_total_inventory_value(products)

    print(f"\nOverall Inventory Value: ${overall_value:.2f}")
