# TODO Дан словарь словарей, ключ внешнего словаря - id пользователя, значение - #  словарь с данными о пользователе
#  (имя, фамилия, телефон, почта), вывести #  имена тех, у кого не указана почта (нет ключа email или значение этого
#  ключа - #  пустая строка)

my_dict = {
    'user_id_1': {'name': 'Alex', 's_name': 'Ivanov', 'phone': '3752900000', 'email': 'alex@alex.com'},
    'user_id_2': {'name': 'Max', 's_name': 'Petrov', 'phone': '3752911111'},
    'user_id_3': {'name': 'Vera', 's_name': 'Ivanova', 'phone': '3752922222', 'email': 'vera@vera.com'},
    'user_id_4': {'name': 'Nasta', 's_name': 'Petrova', 'phone': '3752933333', 'email': ''}

}

for _, data in my_dict.items():
    if not data.get('email'):
        print(data['s_name'], data['name'])
