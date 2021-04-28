def display_supply(array):
    print(f'The coffee machine has:')
    print(f"{array['water']} of water")
    print(f"{array['milk']} of milk")
    print(f"{array['coffee_beans']} of coffee beans")
    print(f"{array['cups']} of disposable cups")
    if not array['money'] == 0:
        print(f"${array['money']} of money\n")
    else:
        print(f"{array['money']} of money\n")


def action(c, array):
    if c == 'remaining':
        display_supply(ingredients)
    elif c == 'buy':
        buy(ingredients)
    elif c == 'fill':
        fill(ingredients)
    elif c == 'take':
        take(ingredients)
    return array


def check_availability(array, items):

    for item, quantity in items.items():
        if array[item] < quantity:
            print(f'Sorry, not enough {item}!\n')
            return False
    print(f"I have enough resources, making you a coffee!\n")
    return True


def making_drink(array, items):
    for item, quantity in items.items():
        array[item] -= quantity
    return array


def buy(array):
    choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
    if choice == '1':
        if check_availability(array, espresso_ingredients):
            array['money'] += 4
            array = making_drink(array, espresso_ingredients)
            array['cups'] -= 1
    elif choice == '2':
        if check_availability(array, latte_ingredients):
            array['money'] += 7
            array = making_drink(array, latte_ingredients)
            array['cups'] -= 1
    elif choice == '3':
        if check_availability(array, espresso_ingredients):
            array['money'] += 6
            array['cups'] -= 1
            array = making_drink(array, cappuccino_ingredients)
    elif choice == 'back':
        main()
        return
    return array


def fill(array):
    water_ml = int(input('Write how many ml of water do you want to add:\n'))
    array['water'] += water_ml

    milk_ml = int(input("Write how many ml of milk do you want to add:\n"))
    array['milk'] += milk_ml

    coffee_gr = int(input("Write how many grams of coffee do you want to add:\n"))
    array['coffee_beans'] += coffee_gr

    disp_cups = int(input('Write how many disposable cups of coffee do you want to add:\n'))
    array['cups'] += disp_cups
    print()
    return array


def take(array):
    print(f"I gave you ${array['money']}\n")
    array['money'] = 0
    return array


ingredients = {
    'water': 400,
    'milk': 540,
    'coffee_beans': 120,
    'cups': 9,
    'money': 550
}

espresso_ingredients = {
    'water': 250,
    'coffee_beans': 16
}

latte_ingredients = {
    'water': 350,
    'milk': 75,
    'coffee_beans': 20
}

cappuccino_ingredients = {
    'water': 200,
    'milk': 100,
    'coffee_beans': 12
}


def main():

    while True:
        command = input('Write action (buy, fill, take, remaining, exit):\n')
        if command == 'exit':
            exit()

        print()
        action(command, ingredients)


main()
