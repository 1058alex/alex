name = input('Your name:')
age = input('Your age in numbers:')
city = input('Your city:')
method_1 = f'Hi, my name is {name}, I am {age} years old, I live in {city}'
print(method_1)
method_2 = 'Hi, my name is ' + name + ', I am ' + age + ' yars old, I live in ' + city + '.'
print(method_2)
method_3 = f'Hi, my name is {name}, I am {age} years old, I live in {city}'.format(name=name, age=age, city=city)
print(method_3)
