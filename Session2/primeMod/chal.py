from Crypto.Util.number import *
from secret import flag

m = bytes_to_long(flag)

n = getPrime(1024)
e = 65537
c = pow(m, e, n)

with open("Session2\primeMod\out.txt", "w") as f:
    f.write(f"n = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"c = {c}\n")