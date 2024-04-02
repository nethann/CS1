class VendingMachine:
    def __init__(self, soda, water, coffee):
        self.soda = soda
        self.water = water
        self.coffee = coffee

    def purchase(self, drink_type):
        if drink_type == 1 and self.soda > 0:
            self.soda -= 1
            print("Purchased a soda.")
        elif drink_type == 2 and self.water > 0:
            self.water -= 1
            print("Purchased water.")
        elif drink_type == 3 and self.coffee > 0:
            self.coffee -= 1
            print("Purchased a soda.")
        else:
            print("Out of stock.")

    def restock(self, drink_type, amount):
        if drink_type == 1:
            self.soda += amount
        elif drink_type == 2:
            self.water += amount
        elif drink_type == 3:
            self.coffee += amount

    def inventory(self):
        print(f"Soda: {self.soda} bottles")
        print(f"Water: {self.water} bottles")
        print(f"Coffee: {self.coffee} bottles")


my_vending_Machine = VendingMachine(9, 10, 10)

while True:
    user_input = input("> ")

    if user_input.lower() == "quit" or user_input.lower() == "q": 
        break

    if user_input.lower() == "buy":
        option = int(input("Please select an option:\n1 - Soda\n2 - Water\n3 - Coffee\n"))
        my_vending_Machine.purchase(option)

    elif user_input.lower() == "restock":
        option = int(input("Please select an option:\n1 - Soda\n2 - Water\n3 - Coffee\n"))
        amount = int(input("Please enter an amount:\n"))
        my_vending_Machine.restock(option, amount)

    elif user_input.lower() == "inventory":
        my_vending_Machine.inventory()
