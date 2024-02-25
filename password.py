import random
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
dlugosc = int(input('długość hasła'))
hasla = ''
for i in range(dlugosc):
    hasla += random.choice(symbols)
print(hasla)