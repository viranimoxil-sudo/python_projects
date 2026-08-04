inventory = {}

def add_item():
    item_id = input("Enter Item ID: ")

    if item_id in inventory:
        print("Item already exists! Please enter different ID")
        return  # stop function here, don't continue below

    name = input("Enter Item Name: ")
    price = float(input("Enter Price: "))
    qty_number = input("Enter Quantity (number): ")
    unit = input("Enter Unit (kg/pcs/litre/dozen): ")

    # category ko dropdown jaisa dikhane ke liye numbered menu
    print("Select Category:")
    print("1. Grocery")
    print("2. Vegetable")
    print("3. Fruit")
    print("4. Dairy")
    print("5. Snacks")

    categories = {
        "1": "Grocery",
        "2": "Vegetable",
        "3": "Fruit",
        "4": "Dairy",
        "5": "Snacks"
    }

    cat_choice = input("Enter category choice (1-5): ")
    category = categories[cat_choice]   # number se category name mil gaya

    inventory[item_id] = {
        "name": name,
        "price": price,
        "quantity": int(qty_number),   # number store, string nahi
        "unit": unit,                  # unit alag se store
        "category": category
    }

    print(f"{name} added successfully!")


def view_item():
    if not inventory:
        print("Your Inventory Is Empty! Pls Add Some Item!")
        return  # stop here if empty

    for key, value in inventory.items():
        print(f"ID: {key} | Name: {value['name']} | Price: ₹{value['price']} | Qty: {value['quantity']} {value['unit']} | Category: {value['category']}")


def update_item():
    item_id = input("Enter Product Id That you want to update: ")

    if item_id not in inventory:
        print("Item Not Found in inventory")
        return  # stop function here, don't continue below

    print("1 - Add Stock")
    print("2 - Remove Stock")
    stock_choice = int(input("Enter Your Choice (1 or 2): "))

    if stock_choice == 1:
        qut = input("How much quantity you want to add: ")
        inventory[item_id]["quantity"] += int(qut)
        print("Stock added successfully!")
    elif stock_choice == 2:
        remove = input("How much quantity you want to remove: ")
        inventory[item_id]["quantity"] -= int(remove)
        print("Stock removed successfully!")
    else:
        print("Invalid choice!")


def delete_item():
    item_id = input("Enter Product ID that you want to delete: ")

    if item_id not in inventory:
        print("Item Not Found in inventory")
        return  # stop function here, don't continue below

    del inventory[item_id]   # entry ko dictionary se hata diya
    print("Item deleted successfully!")

def low_quantity():
    found_low = False   # tracking variable - abhi tak koi low stock item nahi mila

    for key, value in inventory.items():
        if value["quantity"] < 5:
            print(f"⚠️ LOW STOCK: {value['name']} - only {value['quantity']} {value['unit']} left!")
            found_low = True   # bata do ki ek low stock item mil gaya

    if not found_low:
        print("✅ All items have sufficient stock.")

def total_value():
    total = 0
    for key , value in inventory.items():
        total += value['price'] * value['quantity']
        
  
    print(f"Total Inventroy value is : {total}")
    


# ---- MENU LOOP ----
while True:
    print("\n|------MENU------|")
    print("1. Add Item")
    print("2. View Items")
    print("3. Update Stock")
    print("4. Delete Item")
    print("5. Low Stock Alert")
    print("6. Total Inventory value")
    print("7. Exit")



    choice = input("Enter Your Choice (1-7): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        view_item()
    elif choice == "3":
        update_item()
    elif choice == "4":
        delete_item()
    elif choice == "5":
        low_quantity()
    elif choice == "6":
        total_value()
    elif choice == "7":
        print("Exiting program... Goodbye!")
        break   # loop se bahar nikal jayega
    else:
        print("Invalid choice! Please enter 1-7.")