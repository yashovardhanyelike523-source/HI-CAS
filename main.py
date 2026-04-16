from models.item import Item
from models.consumption import Consumption
from utils.validators import validate_expiry
from storage.json_store import save_inventory
from storage.csv_store import save_consumption
from analysis.analyzer import numpy_analysis, pandas_analysis
from visual.charts import show_chart

inventory = []
consumption_log = []


def add_product():
    try:
        name = input("Item name: ")
        qty = float(input("Quantity: "))
        price = float(input("Price: "))
        category = input("Category: ")
        expiry = input("Expiry (DD-MM-YYYY): ")
        if not validate_expiry(expiry):
            print(" Invalid date! erorr in entry please verify")
            return
        inventory.append(Item(name, qty, price, category, expiry))
        print(" Item added successfully!")
    except:
        print(" Invalid input")
def view_products():
    print("\n--- INVENTORY ---")

    if not inventory:
        print("⚠ No items available!")
        return
    for i, item in enumerate(inventory, 1):
        print(f"{i}. {item}")
def consume_product():
    name = input("Enter item name: ")
    try:
        used = float(input("Quantity used: "))
    except:
        print(" Invalid input")
        return
    for item in inventory:
        if item.name.lower() == name.lower():
            if item.quantity < used:
                print(" Not enough stock!")
                return
            item.consume(used)
            consumption_log.append(Consumption(name, used))
            print(" Consumption updated")
            return
    print(" Item not found")
def main():
    while True:
        print("\n====== HI-CAS SYSTEM ======")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Consume Item")
        print("4. Save Data")
        print("5. Analysis")
        print("6. Graph")
        print("7. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            consume_product()
        elif choice == "4":
            save_inventory(inventory)
            save_consumption(consumption_log)
        elif choice == "5":
            numpy_analysis(consumption_log)
            pandas_analysis(consumption_log)
        elif choice == "6":
            show_chart(consumption_log)
        elif choice == "7":
            print(" Exiting program...")
            break
        else:
            print(" Invalid choice")
if __name__ == "__main__":
    main()