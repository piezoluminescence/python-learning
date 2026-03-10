import time
cart = []

class item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class visual:
    def border():
        return print("\n==========\n")
    
    def nocart():
        return print("You do not have anything on your cart!")

class cart:
    def __init__(self):
        self.items = []
    
    def showitems(self):
        if not self.items:
            visual.nocart()
            return 

        total = 0
        for item in self.items:
            print(f"{item.name}, ₱{item.price}")
            total += item.price
        print(f"Total price: ₱{total}")
        return

    def additems(self, name, price):
        material = item(name, price)
        self.items.append(material)
        print("Item added to cart!")
        return
    
    def removeitems(self, name):
        if not self.items:
            visual.nocart()
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print("Item removed from cart!")
                return

    def checkout(self):
        if not self.items:
            visual.nocart()
            return
        print("Checkout:")
        cart.showitems(self)
        optioner = input("\nAre you sure you want to check out? (Y/N): ")
        if optioner.lower() == "y":
            print("Processing purchase...")
            time.sleep(6.7)
            print("Purchase complete! Thank you for shopping.")
            self.items.clear()
        elif optioner.lower() == "n":
            print("Purchase cancelled.")
        else:
            print("Invalid input!")
        return

visuals = visual()
cartwheel = cart()

while True:
    visual.border()
    print("1. Show Cart")
    print("2. Add Item to Cart")
    print("3. Remove Item to Cart")
    print("4. Check Out")
    print("5. Exit\n")

    option = int(input("Enter option: "))

    match option:
        case 1:
            visual.border()
            print("Cart:")
            cartwheel.showitems()
        case 2:
            visual.border()
            name = input("Enter name: ")
            price = float(input("Enter price: "))
            cartwheel.additems(name, price)
        case 3:
            visual.border()
            name = input("Enter name: ")
            cartwheel.removeitems(name)
        case 4:
            visual.border()
            cartwheel.checkout()
        case 5:
            print("Exiting program. Thank you for using the program!")
            break
        case _:
            print("Invalid option!")
