from data import MENU, resources
from art import logo
from time import sleep
                                                                              
machine_is_on = True


def report():
    print(f"\nREPORT\n"
          f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}"
          f"\nPress enter to exit...")
    input()


def resources_manager(choice):
    resources['water'] -= MENU[choice]['ingredients']['water']
    resources['coffee'] -= MENU[choice]['ingredients']['coffee']
    resources['money'] += MENU[choice]['cost']
    if choice == 'latte' or choice == 'cappuccino':
        resources['milk'] -= MENU[choice]['ingredients']['milk']


def check_resources(choice):
    if resources['water'] < MENU[choice]['ingredients']['water']:
        print(f"\nSorry there is not enough water: {resources['water']}ml")
        sleep(5)
        return 0
    if resources['coffee'] < MENU[choice]['ingredients']['coffee']:
        print(f"\nSorry there is not enough coffee: {resources['coffee']}g")
        sleep(5)
        return 0
    if choice == 'latte' or choice == 'cappuccino':
        if resources['milk'] < MENU[choice]['ingredients']['milk']:
            print(f"\nSorry there is not enough milk: {resources['milk']}")
            sleep(5)
            return 0


def order(choice):
    cost = MENU[choice]["cost"]
    print(f"\n{choice.capitalize()} costs: {cost}\nPlease insert coins.")
    coins = 0
    coins += int(input("How many quarters? ($0.25): ")) * 0.25
    coins += int(input("How many dimes? ($0.10): ")) * 0.10
    coins += int(input("How many nickles? ($0.5): ")) * 0.05
    coins += int(input("How many pennies? ($0.1): ")) * 0.01

    if coins == cost:
        print(f"\nHere is your {choice} ☕. Enjoy!")
        sleep(10)
        resources_manager(choice)
    elif coins > cost:
        print(f"\nHere is your {choice} ☕. Enjoy!")
        print(f"You entered ${coins}, {choice} costs: {cost}")
        print(f"And here is ${round(coins - cost, 2)} in charge...")
        sleep(10)
        resources_manager(choice)
    else:
        print(f"\nSorry, that's not enough money: ${round(coins, 2)}.\n"
              f"{choice.capitalize()} costs: ${cost}\n"
              f"Money refunded...")
        sleep(10)


def password_verification():
    print("\n" * 100)
    password = int(input("\nYou entered maintainer profile\nEnter password: "))
    if password == 123:
        return 1
    else:
        print("Wrong password!")
        return 0


def coffee_machine():
    print("\n" * 100)
    print(logo)
    choice = input(f"Hello, what would you like?\n"
                   f"Espresso (${MENU['espresso']['cost']})\n"
                   f"Latte (${MENU['latte']['cost']})\n"
                   f"Cappuccino (${MENU['cappuccino']['cost']})\n"
                   f"Type 'espresso', 'latte' or 'cappuccino': ").lower()

    # Secret words only for maintainers of the coffee machine
    if choice == 'report':
        if password_verification() == 1:
            report()
    elif choice == 'off':
        if password_verification() == 1:
            return 0

    elif choice not in MENU:
        print("\nYou entered incorrect name of the drink. Try again...")
        sleep(5)
    else:
        if check_resources(choice) == 0:
            return
        order(choice)


while machine_is_on:
    machine = coffee_machine()
    if machine == 0:
        print("\n" * 100)
        machine_is_on = False
