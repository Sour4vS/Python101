inventory = {
    "apple": {"price": 2.50, "stock": 10},
    "bread": {"price": 3.00, "stock": 5},
    "milk": {"price": 1.99, "stock": 8},
    "eggs": {"price": 4.50, "stock": 12}
}

cart ={}
print(" ----- available inventory -----")
print(inventory)

start = input("Press e to start shopping...").lower()
if start =="e":
    while True:
        item = input("What would you like to buy? (or type 'checkout'):")
        if item =="checkout".lower():
            break
        else:
            quantity = int(input("how much quantity needed? :"))
            if item not in inventory:
                print("Item is not available..try again")
                continue
            else:
                if quantity > inventory[item]["stock"]:
                    print("Insufficient Stock !")
                else:
                    inventory[item]["stock"]-=quantity
                    if item in cart:
                        cart[item]+=quantity
                    else:
                        cart[item]=quantity
                    print(f"Successfully added {quantity}x {item} to your cart.")
                
print("-----checkout section-----")
subtotal = 0
for item,qauntity in cart.items():
    item_price = inventory[item]["price"]
    item_total = quantity * item_price
    subtotal += item_total

    print(f"Item Name: {item.capitalize():<8} | Quantity: {quantity:<3} | Price: ${item_price:.2f} | Item Total: ${item_total:.2f}")

print("-" * 80)

tax = subtotal * 0.05
grand_total = subtotal + tax

print(f"Subtotal:   ${subtotal:.2f}")
print(f"Tax (5%):   ${tax:.2f}")
print(f"Total Bill: ${grand_total:.2f}")


print("-" * 80)
