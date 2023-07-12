# TODO Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int.

def converter(data):
    new = (bin(eval(data)) if data.isdigit() else eval(data))
    return new


n = input()
converter(n)
print(converter(n))
