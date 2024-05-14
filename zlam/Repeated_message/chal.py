from Crypto.Util.number import *
from secret import flag


m = bytes_to_long(flag)
e = 3
ns = []

def ib3at_la_7abibtak(m, e):
    p = getPrime(256)
    q = getPrime(256)
    n = p * q
    ns.append(n)
    return pow(m, e, n)

cts = [ib3at_la_7abibtak(m, e) for _ in range(3)]

with open("out.txt", "w") as f:
    f.write(f"ns = {ns}\n")
    f.write(f"e = {e}\n")
    f.write(f"cts = {cts}\n")