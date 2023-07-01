# TODO Сделать калькулятор: у пользователя спрашивается число, потом действие и второе

first_amaunt = float(input('type first amount:'))
action = input('type action:')
second_amount = float(input('type second amount:'))
if action == '+':
    print(first_amaunt + second_amount)
elif action == '-':
    print(first_amaunt - second_amount)
elif action == '*':
    print(first_amaunt * second_amount)
elif action == '/':
    print(first_amaunt / second_amount)
elif action == '%':
    print(first_amaunt % second_amount)
elif action == '**':
    print(first_amaunt ** second_amount)
elif action == '//':
    print(first_amaunt % second_amount)
else:
    print('invalible operation')
