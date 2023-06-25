from resources import resources,coffee_cup,coffee_machine

def espresso(water,coffee):
    if water < 50 or coffee < 18:
        print("sorry resources not sufficient and Ur amount is refunded please try again..")
    else:
        bill_statement(amount_to_b_pay,15)
        reduces_resources(50,0,18)
        print("Take ur Espresso and enjoy...!")
        print(coffee_cup)
def latte(water,milk,coffee):
    if water < 200 or coffee < 24 or milk < 150:
        print("sorry resources not sufficient for latte and Ur amount is refunded please try again..")
    else:
        bill_statement(amount_to_b_pay,30)
        reduces_resources(200,150,24)
        print("Take ur latte and enjoy...!")
        print(coffee_cup)
def cappuccino(water,milk,coffee):
    if water < 200 or coffee < 24 or milk < 100:
        print("sorry resources not sufficient for cappuccino and Ur amount is refunded please try again..")
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


water = int(resources["water"])
milk = int(resources["milk"])
coffee = int(resources["coffee"])
turn_off = False

print(coffee_machine)
print(f"\nCost of items:\nEspresso: 15rs/-\nLatte: 30rs/-\nCappuccino: 50rs/-")

while not turn_off:
    ordered=""
    correct_opt = True
    while correct_opt:
        options = ["off","resources","espresso","latte","cappuccino"]
        ordered = input("\nWhat would you like? (Espresso/Latte/Cappuccino): ").lower()
        if not ordered in options:
            print("please order correct item..")
        else:
            correct_opt = False

    if ordered == "off":
        turn_off = True
        print("Machine is powered off")
    else:
        if ordered == "resources":
            ordered_item(ordered)

        else:
            amount_to_b_pay = int(input("please pay the bill: "))
            billing(ordered,amount_to_b_pay)

