# TODO Дан список содержащий в себе различные типы данных, отфильтровать таким
#  образом, чтобы остались только строки, использование дополнительного списка
#  незаконно

some_list = [1, 2, 3, None, 'Sasha', 'Nasta', ' python']
sotr = (obj for obj in some_list if isinstance(obj, str))
print(list(sotr))
