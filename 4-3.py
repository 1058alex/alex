# TODO Заполнить словарь где ключами будут выступать числа от 0 до n,
#  а значениями вложенный словарь с ключами "name" и "email",
#  а значения для этих ключей будут браться с клавиатуры

n = int(input())
data = {j: {'name:': input('name:'), 'email:': input('email:')} for j in range(n)}
print(data)
