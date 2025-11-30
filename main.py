import inventoryManagement as im


def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product Quantity")
        print("3. Display Inventory")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            im.add_product()
        elif choice == '2':
            im.updateQuantity()
        elif choice == '3':
            im.displayInventory()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
