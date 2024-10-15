menu = {
    'Pizza':69,
    'Pasta':59,
    'Burger':59,
    'Coffee':49,
    'Tea':39,
    'Sandwitch':49,
}
print("Welcome to python restaurant.")
print(" Pizza: 69/-\n Pasta: 59/-\n Burger: 59/-\n Coffee: 49/-\n Tea: 39/-\n Sandwitch: 49/-")

order_total = 0
item_1 = input("Enter the name of your order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Ordered item is not available now!")

another_order = input("Do you want to order anything?")
if another_order =='yes':
    item_2 = input("Enter the name of the item:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order.")
    else:
        print(f"Ordered item is not available now!")

print(f"The total amount of items to pay is {order_total}")

