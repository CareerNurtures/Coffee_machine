
from resources import resources,coffee_cup,coffee_machine,MENU

def insufficient_resources():
    print("Resource insufficient in machine")
    print("Your amount is refunded please try again after some time..\n")

def espresso(water,coffee):
    if water < 50 or coffee < 18:
        insufficient_resources()
    else:
        bill_statement(amount_to_b_pay,15)
        reduces_resources(50,0,18)
        print("Take ur Espresso and enjoy...!")
        print(coffee_cup)
def latte(water,milk,coffee):
    if water < 200 or coffee < 24 or milk < 150:
        insufficient_resources()
    else:
        bill_statement(amount_to_b_pay,30)
        reduces_resources(200,150,24)
        print("Take ur latte and enjoy...!")
        print(coffee_cup)
def cappuccino(water,milk,coffee):
    if water < 200 or coffee < 24 or milk < 100:
        insufficient_resources()
    else:
        bill_statement(amount_to_b_pay,50)
        reduces_resources(200, 100, 24)
        print("Take ur Cappuccino and enjoy...!")
        print(coffee_cup)

def ordered_item(order):

    if order == "espresso":
        espresso(water,coffee)

    elif order == "latte":
        latte(water,milk,coffee)

    elif order == "cappuccino":
        cappuccino(water,milk,coffee)

    elif order == "resources":
        print(f" Water : {water}\n Milk : {milk}\n coffee : {coffee}")


def bill_statement(amount,cost_of_order):
    left_amount = amount - cost_of_order
    print(f"Here is ur change : {left_amount}")


def billing(order,amount):
    if order == "espresso" and (amount<15 or amount<0):
        print("Insufficient amount Ur amount is refunded please try again..")

    elif order == "latte" and (amount < 30 or amount < 0):
        print("Insufficient amount Ur amount is refunded please try again..")

    elif order == "cappuccino" and (amount < 50 or amount < 0):
        print("Insufficient amount Ur amount is refunded please try again..")
    else:
        ordered_item(order)


def reduces_resources(req_water,req_milk,req_coffee):
    global water,milk,coffee
    water -= req_water
    milk -= req_milk
    coffee -= req_coffee

def display_menu():
    print("Menu:")
    for drink, details in MENU.items():
        cost = details['cost']
        print(f"{drink.capitalize()}: {cost}rs/-")

water = int(resources["water"])
milk = int(resources["milk"])
coffee = int(resources["coffee"])

turn_off = False

print(coffee_machine)

while not turn_off:
    ordered=""
    while True:
        options = ["off","resources","espresso","latte","cappuccino"]
        display_menu()
        ordered = input("\nWhat would you like?(Enter 'off' to turn off the machine): ").lower()
        if not ordered in options:
            print("please order correct item..\n")
        else:
            break

    if ordered == "off":
        turn_off = True
        print("Machine is powered off")
    else:
        if ordered == "resources":
            ordered_item(ordered)

        else:
            payment_completed = False
            while not payment_completed:
                amount_to_b_pay = input("please pay the bill: ").split(".")
                if amount_to_b_pay[0].isdigit():
                    amount_to_b_pay = int(amount_to_b_pay[0])
                    billing(ordered, amount_to_b_pay)
                    payment_completed = True
                else:
                    print("Please enter Amount with out any Characters")

