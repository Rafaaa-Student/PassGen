import random

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
f = int(input("Masukkan berapa angka Password yang kamu inginkan?"))

random_string = ""
for i in range(f):
    random_string += random.choice(chars)

print(random_string)
