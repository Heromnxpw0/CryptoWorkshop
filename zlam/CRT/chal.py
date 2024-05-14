from Crypto.Util.number import *
from secret import flag


flag = bytes_to_long(flag)
flag = bin(flag)[2:]

# the length of each block is very very very very very very important
flag = [int(flag[i : i + 64], 2) for i in range(0, len(flag), 64)]

assert len(flag) == 5

coefs = flag + [getRandomInteger(64) for _ in range(14)]

def f(x):
    return sum([c * x**i for i, c in enumerate(coefs)])

xs = [getPrime(128) for _ in range(20)]

out = [f(x) for x in xs]

with open("out.txt", "w") as f:
    f.write(f"xs = {xs}\n")
    f.write(f"out = {out}\n")