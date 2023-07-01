# TODO Вывести первые N цисел кратные M и больше K

n = int(input('amount:'))
m = int(input('divisor:'))
k = int(input('start'))
while n:
    if k % m == 0:
        n -= 1
        print(k)
    k += 1
