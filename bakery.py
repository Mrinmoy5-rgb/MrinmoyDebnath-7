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


print("Menu:")
for number, (item, price) in menu.items():
    print(f"{number}. {item}: ₹{price}")


customer_id = 1
customer_name = input("Enter your name: ")
order_numbers = list(map(int, input("Enter the numbers of your order (comma-separated): ").split(", ")))


order_list = [menu[number][0] for number in order_numbers]
total_price = sum(menu[number][1] for number in order_numbers)
receipt = {
    "Customer ID": customer_id,
    "Customer Name": customer_name,
    "Order List": order_list,
    "Total Price": total_price
}


print("\nReceipt:")
print(f"Customer ID: {receipt['Customer ID']}")
print(f"Customer Name: {receipt['Customer Name']}")
print("Order List:")
for item in receipt['Order List']:
    print(f"{item}: ₹{menu[[i for i, v in menu.items() if v[0] == item][0]][1]}")
print(f"Total Price: ₹{receipt['Total Price']}")
 