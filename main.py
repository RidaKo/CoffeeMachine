from drinks import resources, MENU
from art import bunny_girl
import functions
def main():
    print(" ")
    print("Hey there boy, what would you like?")
    choice =  functions.pick_drink(MENU)
    if choice is None:
        functions.report()
        main()
    elif choice is False:
        print("Goodbye little man. *kiss on the cheek*")
        return None
    else:
        drink_type, drink = choice

    # check if the resources are sufficient
    if not functions.check_resources(drink):
        return None
    # check the amount of money that has been put in and give change
    if not functions.transaction_state(functions.request_money(), drink):
        main()
    functions.deduct_resources(drink)
    print(f"Here is your {drink_type}, master, please enjoy your stay")
    main()
print(bunny_girl)
resources["money"] = 0
main()


