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

    print("\n Changes saved successfully!")
    



def removeItem():

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



