from Crypto.Util.number import *
from secret import flag, message
from sympy.ntheory.modular import crt


"""
A celestial being approached you and presented you with a puzzle:
Within these primes my age is concealed, and my message is encrypted. the chinese know the way for do you?
"""

flag = bytes_to_long(flag)

p = getPrime(256)
q = getPrime(200)
n = p * q * 7 * 11 * 13

h1 = flag % p
h2 = flag % q

with open("out.txt", "w") as f:
    f.write(f"p = {p}\n")
    f.write(f"q = {q}\n")
    f.write(f"h1 = {h1}\n")
    f.write(f"h2 = {h2}\n")