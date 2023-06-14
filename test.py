#







text = input('Enter your text: ')
first_spase = text.find(' ')
last_spase = text.rfind(' ')
word1 = text[:first_spase]
word2 = text[first_spase+1:last_spase]
word3 = text[last_spase+1:]
print(word1)
print(word2)
print(word3)

