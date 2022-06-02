import data_file

profit = 0
is_on = True

while is_on:
    question = input("What would you like?: \n1: espresso\n2: latte\n3: cappuccino")
    if question == 'off':
        is_on = False
    elif question == "report":
        print(f'water: {data_file.resources["water"]} ml')
        print(f'milk: {data_file.resources["milk"]} ml')
        print(f'coffee: {data_file.resources["coffee"]} g')
        print(f'profit is: ${profit}')
    else:
        drink = data_file.MENU[question]
        #some text

