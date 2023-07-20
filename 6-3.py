# TODO Дан список чисел и на вход поступает число N, необходимо сместить список на
#  указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

some_list = [1, 2, 3, 4, 5, 6, 7]
N = int(input('Type N: '))
new_list = some_list[-N:] + some_list[:-N]
print(new_list)


# or via function


def changed(list_f, n):
    return list_f[-n:] + list_f[:-n]


print(changed(some_list, N))
