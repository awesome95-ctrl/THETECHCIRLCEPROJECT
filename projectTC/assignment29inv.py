print("\n---inventory management")
print("1. Add product")
print("2. view inventory")
print("3. update product")
print("4. Delete")
print("5. exit")

choice = input("enter choice")

if choice == "1":
    product__name = input("enter product name:")
    quantity = int(input("enter quantity desired"))
    price = float(input("enter price"))
    inventory.add_product(product_name, quantity, price)

elif choice == "2":
    inventory.view_inventory()

elif choice == "3":
    product_name = input("enter product name")
    quantity = input("enter new quantity(if none skip)")
    price = input("enter new price (if old skip)")

    quantity= int(quantity) if quantity else None
    price = float(price) if price else None
    inventory.update_productvt(product_name, quantity, price)

elif choice =="4":
    product_name = input("enter product name")
    inventory.delete_product(product_name)

elif choice =="5":
    print("Exiting...")
    
else:
    print("invalid choice, please try again")

if__name__=="__main__"  
    # main_menu()

