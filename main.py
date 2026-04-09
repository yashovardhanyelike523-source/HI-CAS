import json
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


inventory_data = []
consumption_log = []


def add_product():
    try:
        name = input("Item name: ")
        qty = float(input("Quantity: "))
        price = float(input("Price: "))
        category = input("Category: ")
        expiry = input("Expiry: ")

        inventory_data.append({
            "name": name,
            "qty": qty,
            "price": price,
            "category": category,
            "expiry": expiry
        })

        print(" Item added successfully!")

    except:
        print(" Invalid input")


def view_products():
    print("\n--- INVENTORY ---")

    if not inventory_data:
        print(" No items available!")
        return

    for i, item in enumerate(inventory_data, 1):
        print(f"{i}. {item['name']} | {item['qty']} | ₹{item['price']} | {item['category']} | Exp: {item['expiry']}")


def consume_product():
    name = input("Enter item name: ")
    try:
        used = float(input("Quantity used: "))
    except:
        print("Invalid input")
        return

    for item in inventory_data:
        if item["name"].lower() == name.lower():
            if item["qty"] < used:
                print(" Not enough stock!")
                return

            item["qty"] -= used
            consumption_log.append({"name": name, "used": used})

            print(" Consumption updated")
            return

    print(" Item not found")


def save_data():
    with open("inventory.json", "w") as f:
        json.dump(inventory_data, f, indent=4)

    with open("consumption.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Item", "Used"])
        for c in consumption_log:
            writer.writerow([c["name"], c["used"]])

    print(" Data saved successfully!")


def load_data():
    global inventory_data

    try:
        with open("inventory.json") as f:
            inventory_data = json.load(f)

        print(" Data loaded successfully!")

    except:
        print(" No saved data found")


def numpy_analysis():
    if not consumption_log:
        print(" No consumption data")
        return

    values = [c["used"] for c in consumption_log]
    arr = np.array(values)

    print("\n--- NUMPY ANALYSIS ---")
    print("Average usage:", np.mean(arr))
    print("Max usage:", np.max(arr))
    print("Min usage:", np.min(arr))


def pandas_analysis():
    if not consumption_log:
        print(" No consumption data")
        return

    df = pd.DataFrame(consumption_log)

    print("\n--- PANDAS REPORT ---")
    print(df.groupby("name")["used"].sum())


def show_chart():
    if not consumption_log:
        print("⚠ No data for graph")
        return

    df = pd.DataFrame(consumption_log)
    summary = df.groupby("name")["used"].sum()

    summary.plot(kind="bar")
    plt.title("Consumption Chart")
    plt.xlabel("Items")
    plt.ylabel("Usage")
    plt.show()


def main_menu():
    while True:
        print("\n====== HI-CAS SYSTEM ======")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Consume Item")
        print("4. Save Data")
        print("5. Load Data")
        print("6. NumPy Analysis")
        print("7. Pandas Analysis")
        print("8. Show Graph")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            consume_product()
        elif choice == "4":
            save_data()
        elif choice == "5":
            load_data()
        elif choice == "6":
            numpy_analysis()
        elif choice == "7":
            pandas_analysis()
        elif choice == "8":
            show_chart()
        elif choice == "9":
            print(" Exiting program...")
            break
        else:
            print(" Invalid choice")


main_menu()