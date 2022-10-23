from drinks import resources, MENU


def pick_drink(MENU) -> tuple:
    """asks what type of drink do you want"""

    drink = input("Perhaps a kind of drink?(espresso/latte/cappuccino/or maybe a little somethin' special... ): ").casefold()
    if (drink == "off"):
        return False
    elif(drink == "report"):
        return None
    else:
        for key  in MENU:
            if key == drink:
                drink_type = key
                drink = MENU[drink]
        return drink_type, drink

def report()-> None:
    """Prints out the resources of the vending machine"""
    print(f'Water: {resources["water"]} ml')
    print(f"Milk {resources['milk']} ml")
    print(f'Coffee: {resources["coffee"]} g')
    print(f'Money: ${resources["money"]}')

def check_resources(drink) -> bool :
    """Checks whether there are sufficient resources in the vending machine """
    resource_enough = True
    for resource in resources:
        if resource == "money":
            continue
        if resources[resource] <= drink["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}")
            resource_enough = False
    return resource_enough

def request_money() -> float:
    """request to input money in coins"""
    print("Please insert the coins..")
    total_money = 0
    total_money = total_money + 0.25 * int(input("How many quarters?"))
    total_money = total_money + 0.10 * int(input("How many dimes?"))
    total_money = total_money + 0.05 * int(input("How many nickles?"))
    total_money = total_money + 0.01 * int(input("How many pennies?"))
    return total_money

def transaction_state(money, drink) -> bool:
    """Checks if the user has put in the correct amount of money
    """
    if money < drink["cost"]:
        print("I am sorry that is not enough money, the amount you put in will be returned")
        return False
    elif money == drink["cost"]:
        return True
    elif money >drink["cost"]:
        change = money - drink["cost"]
        print(f"You have put in to much money. Your change is ${change}")
        return True

def deduct_resources(drink):
    """ Gives money and deducts resources needed for the making of the coffee"""
    for resource in resources:
        if resource == "money":
            resources[resource] = resources[resource] + drink["cost"]
        else:
            resources[resource] = resources [resource] - drink["ingredients"][resource]
