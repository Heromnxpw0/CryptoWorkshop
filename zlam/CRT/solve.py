from sympy.ntheory.modular import crt
from Crypto.Util.number import *
with open("zlam\CRT\out.txt", "r") as f:
    xs = eval(f.readline().split(" = ")[1])
    out = eval(f.readline().split(" = ")[1])
    

f = []

for i in range(1, 6):
    mods = xs[:]
    a = [out[j] % mods[j] for j in range(len(xs))]
    c = crt(mods, a)[0]
    if i != 5:
        f.append(format(c, "064b"))
    else:
        f.append(bin(c)[2:])
    out = [out[j] - c for j in range(len(xs))]
    out = [out[j] // xs[j] for j in range(len(xs))]
    

f = "".join(f)
print(long_to_bytes(int(f, 2)))
