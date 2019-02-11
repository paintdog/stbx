from string import ascii_lowercase, ascii_uppercase, digits
import random

sonderzeichen = [a for a in "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"]
sonderzeichen = [a for a in "!#$%&():<=>?@_{|}"]
sonderzeichen = [a for a in "!#$%&:=@_"]
sonderzeichen = [a for a in "_"]

kleinbuchstaben = [a for a in ascii_lowercase]

grossbuchstaben = [a for a in ascii_uppercase]

zahlen = [a for a in digits]

for i in range(30):

    a = random.choice([1, 2])        # Sonderzeichen
    b = random.choice([4, 5, 6, 7, 8])  # Kleinbuchstaben
    c = random.choice([4, 5, 6, 7, 8])  # Großbuchstaben
    d = random.choice([3, 4])  # Zahlen

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
