# /////////////////////////////////////////////////////DATA

inventory = {
    "apple": {
        "quantity": 10,
        "price": 0.50,
        "id": 1,
        "category": "food",
        "brand": "No-Brand"
    },
    "milk": {
        "quantity": 5,
        "price": 1.20,
        "id": 2,
        "category": "drinks",
        "brand": "Nestlé"
    },
    "bread": {
        "quantity": 8,
        "price": 2.30,
        "id": 3,
        "category": "food",
        "brand": "Quaker"
    },
    "eggs": {
        "quantity": 12,
        "price": 3.50,
        "id": 4,
        "category": "food",
        "brand": "No-Brand"
    },
    "water": {
        "quantity": 20,
        "price": 0.90,
        "id": 5,
        "category": "drinks",
        "brand": "Pepsi"
    },
    "cheese": {
        "quantity": 6,
        "price": 4.25,
        "id": 6,
        "category": "food",
        "brand": "Kellogg's"
    },
    "banana": {
        "quantity": 15,
        "price": 0.35,
        "id": 7,
        "category": "snacks",
        "brand": "No-Brand"
    },
    "coffee": {
        "quantity": 3,
        "price": 6.99,
        "id": 8,
        "category": "drinks",
        "brand": "Starbucks"
    },
    "rice": {
        "quantity": 18,
        "price": 1.10,
        "id": 9,
        "category": "food",
        "brand": "Heinz"
    },
    "cereal": {
        "quantity": 7,
        "price": 3.80,
        "id": 10,
        "category": "food",
        "brand": "Coca-Cola"
    }
}

categories = ["food", "drinks", "cleaning", "snacks", "others"]
brand_info = ("Coca-Cola", "Kellogg's", "Starbucks", "Nestlé", "Pepsi", "Heinz", "Quaker","No-Brand")
product_ids = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# ///////////////////////////////////////////////////////////////functions

def get_new_id():
    return max(product_ids) + 1

def printHeader():
    header = f"{'ID':<10}{'Item':<20} {'Quantity':<20} {'Price':<20}  {'Category':<20} {'Brand':<20}"
    print(f"{header:^130}")

def printRow(item, quantity, price, product_id, category, brand):
    item = f"{item}"
    quantity = f"{quantity}"
    price = f"{price}"
    product_id = f"{product_id}"
    category = f"{category}"
    brand = f"{brand}"

    table = f"{product_id:<10}{item:<20} {quantity:<20} {price:<20}  {category:<20} {brand:<20}"
    print(f"{table:^130}")


def viewInventory():
    
    print(" ")
    printHeader()

    for item, values in inventory.items():
        item = f"{item}"
        quantity = f"{values['quantity']}"
        price = f"{values['price']}"
        product_id = f"{values['id']}"
        category = f"{values['category']}"
        brand = f"{values['brand']}"

        table = f"{product_id:<10}{item:<20} {quantity:<20} {price:<20}  {category:<20} {brand:<20}"
        print(f"{table:^130}") 


def addItem():
    add = input("do you wanna add a item? Y/N: ").lower()

    while add not in ("y", "n"):
        print("Invalid option. Type Y or N.")
        add = input("do you wanna add a item? Y/N: ").lower()


    if add == "n":
        menu()
    elif add == "y":
        while True:
            addItem = input("Insert the item name: ").strip()
            if addItem.replace(" ", "").isalnum():
                break
            else: print("Invalid option. Please try again.")

        
        while True:
            addQuantity = input("Insert the quantity: ").strip()
            if addQuantity.isdigit():  
                addQuantity = int(addQuantity)
                break
            else: print("Invalid option. Please try again.")
# ////////////////////////////////////////////////////////////TRY AND EXCEPT FOR EXTRA POINTS hahhahahahaha
        while True:
            addPrice = input("Insert the price: ").strip()
            try:
                addPrice = float(addPrice)
                break
            except ValueError:
                print("Invalid price. Use numbers like 3 or 3.50")


        
        AddId = max(product_ids) + 1 

            # category
        print(" ")
        print("Choose a category eg:(1, 2, 3, 4)")
        for idx, category in enumerate(categories, start=1):
            print(idx, category)
        while True:
            category = input("Category: ").strip()
            if category.isdigit() and int(category) in range(1, len(categories) + 1):
                selected_category = categories[int(category) - 1]
                print("Selected category:", selected_category)
                break
            else:
                print("Invalid option. Please choose a valid number.")

        # brand
        print(" ")
        print("Choose a brand eg:(1, 2, 3, 4)")
        for idx, brand in enumerate(brand_info, start=1):
            print(idx, brand)
        while True:
            brand = input("Brand: ").strip()
            if brand.isdigit() and int(brand) in range(1, len(brand_info) + 1):
                selected_brand = brand_info[int(brand) - 1]
                print("Selected brand:", selected_brand)
                break
            else:
                print("Invalid option. Please choose a valid number.")




        print("review:")
        printHeader()
        printRow(addItem, addQuantity, addPrice, AddId, selected_category, selected_brand)
        addConfirm = str(input("confirm add? Y/N : "))
        addConfirm = addConfirm.lower()
        if addConfirm == "n":
            print("item not added")
            input("\nPress ENTER to return to the menu...")
            menu()
        elif addConfirm == "y":
            inventory[addItem] = {"quantity": addQuantity, "price": addPrice, "id": AddId, "category": selected_category, "brand": selected_brand}
            product_ids.add(AddId)
            print("New item adde succesfully")
    
    input("\nPress ENTER to return to the menu...")
    menu()
    

def updateItem():
    global inventory
    viewInventory()
    while True:
        search = input("\nInsert the ID you want to update (or 0 to cancel): ").strip()
        if search == "0":
            print("Update cancelled")
            return
        if search.isdigit():
            search_id = int(search)
            found = None
            for item, values in inventory.items():
                if values["id"] == search_id:
                    found = item
                    break
            if found:
                itemName = found
                break
            else:
                print("ID not found, try again.")
        else:
            print("Only numbers allowed for ID. Try again.")

    current = inventory[itemName]
    temp = current.copy()
    temp_item_name = itemName

    print("\nSelected item:")
    printHeader()
    printRow(itemName, current["quantity"], current["price"], current["id"], current["category"], current["brand"])

    print("\nWhat do you want to update?")
    print("1. Item name")
    print("2. Quantity")
    print("3. Price")
    print("4. Category")
    print("5. Brand")
    print("0. Cancel")

    option = input("Select an option: ").strip()
    if option == "0":
        print("Update cancelled")
        return

    if option == "1":
        while True:
            newName = input("Insert the new item name: ").strip()
            if not newName.replace(" ", "").isalnum():
                print("Invalid name. Only letters, try again.")
            elif newName in inventory and newName != itemName:
                print("This item already exists, try another name.")
            else:
                break
        temp_item_name = newName

    elif option == "2":
        while True:
            newQty = input("Insert the new quantity: ").strip()
            if newQty.isdigit():
                temp["quantity"] = int(newQty)
                break
            print("Invalid quantity, try again.")

    elif option == "3":
        while True:
            newPrice = input("Insert the new price: ").strip()
            if newPrice.replace(".", "", 1).isdigit():
                temp["price"] = float(newPrice)
                break
            print("Invalid price. Example: 3 or 3.50")

    elif option == "4":
        print("\nAvailable Categories:")
        for idx, cat in enumerate(categories, start=1):
            print(idx, cat)
        while True:
            catOpt = input("Select category: ").strip()
            if catOpt.isdigit() and int(catOpt) in range(1, len(categories) + 1):
                temp["category"] = categories[int(catOpt) - 1]
                break
            print("Invalid selection, try again.")

    elif option == "5":
        print("\nAvailable Brands:")
        for idx, brand in enumerate(brand_info, start=1):
            print(idx, brand)
        while True:
            brandOpt = input("Select brand: ").strip()
            if brandOpt.isdigit() and int(brandOpt) in range(1, len(brand_info) + 1):
                temp["brand"] = brand_info[int(brandOpt) - 1]
                break
            print("Invalid selection, try again.")

    print("\nReview before saving:")
    printHeader()
    printRow(temp_item_name, temp["quantity"], temp["price"], temp["id"], temp["category"], temp["brand"])

    confirm = input("\nDo you want to SAVE changes? Y/N: ").strip().lower()
    while confirm not in ("y", "n"):
        print("Invalid option. Type Y or N.")
        confirm = input("Do you want to SAVE changes? Y/N: ").strip().lower()

    if confirm == "n":
        print("Changes cancelled, nothing was updated.")
        input("\nPress ENTER to return to the menu...")

        return

    if temp_item_name != itemName:
        inventory.pop(itemName)
        inventory[temp_item_name] = temp
    else:
        inventory[itemName] = temp

    print("\n Changes saved successfully!")
    
    # #sort inventory
    inventory
    inventory = dict(sorted(inventory.items(), key=lambda x: x[1]["id"]))
    input("\nPress ENTER to return to the menu...")




def removeItem():
    viewInventory()

    while True:
        search = input("\nInsert the ID you want to remove (or 0 to cancel): ").strip()
        if search == "0":
            print("Remove cancelled")
            return

        if search.isdigit():
            search_id = int(search)
            found = None
            for item, values in inventory.items():
                if values["id"] == search_id:
                    found = item
                    break

            if found:
                break
            else:
                print("ID not found, try again.")
        else:
            print("Only numbers allowed for ID. Try again.")

    print("\nSelected item:")
    printHeader()
    values = inventory[found]
    printRow(found, values["quantity"], values["price"], values["id"], values["category"], values["brand"])

    confirm = input("\nDo you want to DELETE this item? Y/N: ").strip().lower()
    while confirm not in ("y", "n"):
        print("Invalid option. Type Y or N.")
        confirm = input("Do you want to DELETE this item? Y/N: ").strip().lower()

    if confirm == "n":
        print("Item was not removed.")
        return

    removed_id = inventory[found]["id"]
    inventory.pop(found)
    if removed_id in product_ids:
        product_ids.remove(removed_id)

    print("Item removed successfully!")


def saveAndExit():
   
    print("Exiting program...")
    exit()  



def showDataType():
    print(" ")
    header = f"{'Item':<25} {'Quantity':<25} {'Price':<25}"
    print(f"{header:^100}")
    for item, values in inventory.items():
        item = f"{item} {type(item)}"
        quantity = f"{values['quantity']} {type(values['quantity'])}"
        price = f"{values['price']} {type(values['price'])}"

        table = f"{item:<25} {quantity:<25} {price:<25}"
        print(f"{table:^100}")

def center(text):
    return text.center(100)


def indent(text):
    return " " * 37 + text  


# ///////////////////////////////////////////////////////////////////menu
def menu():
    print(center("WELCOME TO NELSON SUPER DUPPER INVENTORY PROGRAM"))
    print(center("========== MENU =========="))
    print(indent("1. View Inventory"))
    print(indent("2. Add Item"))
    print(indent("3. Update Item"))
    print(indent("4. Remove Item"))
    print(indent("5. ShowCase Data Type"))
    print(indent("6. Exit and SAVE"))
    print(indent("0. Exit program----NO SAVE!"))
    print(center("=========================="))

    option = input(indent("Select an option: "))

    if option == "1":
        viewInventory()
        input("\nPress ENTER to return to the menu...")
    elif option == "2":
        addItem()
    elif option == "3":
        updateItem()
    elif option == "4":
        removeItem()
        input("\nPress ENTER to return to the menu...")
    elif option == "5":
        showDataType()
        input("\nPress ENTER to return to the menu...")
    elif option == "6":
        saveAndExit()

    elif option == "0":
        print(center("Exiting program..."))
        return
    else:
        print(center("Invalid option. Try again."))
    menu()



menu()



