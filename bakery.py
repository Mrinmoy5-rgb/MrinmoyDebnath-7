from datetime import datetime

RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"

menu = {
    1: ("Samosa", 20),
    2: ("Kachori", 25),
    3: ("Jalebi", 30),
    4: ("Gulab Jamun", 35),
    5: ("Rasgulla", 40),
    6: ("Peda", 50),
    7: ("Ladoo", 55),
    8: ("Barfi", 60),
    9: ("Pakora", 45),
    10: ("Chocolate Truffle", 70)
}

print(CYAN + "=" * 55)
print("            WELCOME TO SWEET & SNACK SHOP")
print("=" * 55 + RESET)

print("\n" + CYAN + "MENU:" + RESET)
print("-" * 55)
print("No   Item Name              Price (₹)")
print("-" * 55)

for num, (item, price) in menu.items():
    print(f"{num:<4} {item:<22} ₹{price}")

print("-" * 55)

customer_id = 1
customer_name = input(YELLOW + "\nEnter Customer Name: " + RESET).strip()

while True:
    orders = {}

    while True:
        try:
            item_no = int(input(YELLOW + "\nEnter Item Number: " + RESET))
            if item_no not in menu:
                print(RED + "Invalid item number." + RESET)
                continue

            qty = int(input(YELLOW + "Enter Quantity: " + RESET))
            if qty <= 0:
                print(RED + "Quantity must be greater than 0." + RESET)
                continue

            orders[item_no] = orders.get(item_no, 0) + qty

            more = input(YELLOW + "Add more items? (Y/N): " + RESET).lower()
            if more != 'y':
                break

        except ValueError:
            print(RED + "Please enter valid numeric input." + RESET)

    print(CYAN + "\nORDER SUMMARY" + RESET)
    print("-" * 55)

    total = 0
    for item_no, qty in orders.items():
        item, price = menu[item_no]
        item_total = qty * price
        total += item_total
        print(f"{item:<22} Qty: {qty:<3} Total: ₹{item_total}")

    print("-" * 55)
    print(GREEN + f"Current Total: ₹{total}" + RESET)

    confirm = input(YELLOW + "\nConfirm order? (Y/N): " + RESET).lower()
    if confirm == 'y':
        break
    else:
        print(RED + "\nOrder cancelled. Please re-enter your order." + RESET)

now = datetime.now()
invoice_no = now.strftime("INV%Y%m%d%H%M%S")
date_time = now.strftime("%d-%m-%Y %I:%M:%S %p")

print("\n" + CYAN + "=" * 55)
print("                    FINAL RECEIPT")
print("=" * 55 + RESET)

print(f"Invoice No    : {invoice_no}")
print(f"Date & Time   : {date_time}")
print(f"Customer ID   : {customer_id}")
print(f"Customer Name : {customer_name}")
print("-" * 55)

print("Item Name              Qty   Price   Total")
print("-" * 55)

grand_total = 0
for item_no, qty in orders.items():
    item, price = menu[item_no]
    total = qty * price
    grand_total += total
    print(f"{item:<22} {qty:<5} ₹{price:<6} ₹{total}")

print("-" * 55)
print(GREEN + f"GRAND TOTAL: ₹{grand_total}" + RESET)
print(CYAN + "=" * 55 + RESET)

print(GREEN + "\nThank you for shopping with us!" + RESET)
