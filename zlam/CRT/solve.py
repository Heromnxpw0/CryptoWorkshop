from sympy.ntheory.modular import crt
from Crypto.Util.number import *
from secret import flag
with open("zlam\CRT\out.txt", "r") as f:
    xs = eval(f.readline().split(" = ")[1])
    out = eval(f.readline().split(" = ")[1])
    


flag = bytes_to_long(flag)
flag = bin(flag)[2:]
print(len(flag))
flag_bites = [flag[i : i + 64] for i in range(0, len(flag), 64)]
flag = [int(flag[i : i + 64], 2) for i in range(0, len(flag), 64)]

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
    

print(len(f))
print(f)
print([len(f[i]) for i in range(5)])
print(flag_bites)
print([f[i] == flag_bites[i] for i in range(5)])
f = "".join(f)
print(long_to_bytes(int(f, 2)))
