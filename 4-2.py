text = input('Type text: ')
data = {text[a]: text.count(text[a]) for a in range(len(text))}
print(data)
