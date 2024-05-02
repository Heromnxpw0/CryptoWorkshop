from Crypto.Util.number import *
import random
from secret import flag

flag = bytes_to_long(flag)
primes = [getPrime(256) for _ in range(25)]


assert len(primes) == len(set(primes))
assert len(bin(flag)) - 2 < 256

hint = [random.choice(primes) * random.choice(primes) for _ in range(50)]

num = 1
for p in random.choices(primes, k = 12):
    num *= p

ct = num * flag
with open("out.txt", "w") as f:
    f.write(f"hint = {hint}\n")        
    f.write(f"ct = {ct}")