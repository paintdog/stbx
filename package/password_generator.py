from string import ascii_lowercase, ascii_uppercase, digits
import random


a = 1  # Sonderzeichen
b = 4  # Kleinbuchstaben
c = 3  # Großbuchstaben
d = 4  # Zahlen


sonderzeichen = [a for a in "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"]
sonderzeichen = [a for a in "!#$%&():<=>?@_{|}"]
sonderzeichen = [a for a in "!#$%&:=@_"]

kleinbuchstaben = [a for a in ascii_lowercase]

grossbuchstaben = [a for a in ascii_uppercase]

zahlen = [a for a in digits]

random.shuffle(sonderzeichen)
random.shuffle(kleinbuchstaben)
random.shuffle(grossbuchstaben)
random.shuffle(zahlen)

result = []
result.extend(sonderzeichen[:a])
result.extend(kleinbuchstaben[:b])
result.extend(grossbuchstaben[:c])
result.extend(zahlen[:d])

random.shuffle(result)
print("".join(result))


'''
print(sonderzeichen)
print(kleinbuchstaben)
print(grossbuchstaben)
print(zahlen)
'''
