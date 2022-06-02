import data_file

profit = int(0)
is_on = True

#проверяем есть ли нужно количество ингредиентов для напитка
def check_resources(order_ingradients):
    for i in order_ingradients:
        if order_ingradients[i] >= data_file.resources[i]:
            print(f'Sorry there is not enough {i}')
            return False
    return True

#Узнаем сколько денег закинет пользователь в кофемат
def process_coins():
    print('Pleace, insert the coins')
    total = int(input('How you have 0.25?')) * 0.25
    total += int(input('How you have 0.1?')) * 0.1
    total += int(input('How you have 0.05?')) * 0.05
    total += int(input('How you have 0.01?')) * 0.01
    return total

#Проверяяем валидность транзакции
def check_transaction(money_received, drink_coast):
    global profit
    if money_received >= drink_coast:
        profit += money_received
        change = round(money_received - drink_coast, 2)
        print(f'Here is your change: ${change}')
        return True
    else :
        print("Sorry that's not enough money. Money refunded")
        return False

#Создаем кофе и вычитаем из реурса использованные ингредиенты
def make_coffee(drink_name, order_ingredients):
    for i in order_ingredients:
        data_file.resources[i] -= order_ingredients[i]
    print('Is your coffee ☕')

while is_on:
    question = input("What would you like?: \n1: espresso\n2: latte\n3: cappuccino\n")
    if question == 'off':
        is_on = False
    elif question == "report":
        print(f'water: {data_file.resources["water"]} ml')
        print(f'milk: {data_file.resources["milk"]} ml')
        print(f'coffee: {data_file.resources["coffee"]} g')
        print(f'profit is: ${profit}')
    else:
        drink = data_file.MENU[question]
        if check_resources(drink['ingredients']):
            pyment = process_coins()
            if check_transaction(pyment, drink['cost']):
                make_coffee(question, drink['ingredients'])

