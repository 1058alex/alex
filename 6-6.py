# TODO Дан список рандомных чисел, необходимо отсортировать его в виде, сначала четные, потом нечётные.
import random


def sorter_fun(data):
    even = []
    odd = []

    for value in sorted(data):
        if value % 2 == 0:
            even.append(value)
        else:
            odd.append(value)

    combined = even + odd
    return combined


random_numbers = [random.randint(1, 100) for _ in range(20)]
sorter_fun(random_numbers)
print(sorter_fun(random_numbers))
