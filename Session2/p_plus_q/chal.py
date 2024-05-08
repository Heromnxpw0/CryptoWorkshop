from Crypto.Util.number import *
from secret import flag

p = getPrime(1024)
q = getPrime(1024)

n = p * q
e = 65537
m = bytes_to_long(flag)
c = pow(m, e, n)

hint = p + q

with open("out.txt", "w") as f:
    f.write(f"n = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"c = {c}\n")
    f.write(f"hint = {hint}\n")

