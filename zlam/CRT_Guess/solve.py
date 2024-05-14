from Crypto.Util.number import *
from sympy.ntheory.modular import crt

with open("zlam\CRT_Guess\out.txt", "r") as f:
    p = int(f.readline().strip().split(" = ")[1])
    q = int(f.readline().strip().split(" = ")[1])
    h1 = int(f.readline().strip().split(" = ")[1])
    h2 = int(f.readline().strip().split(" = ")[1])
    

for i in range(7):
    for j in range(11):
        for k in range(13):
            flag = crt([p, q, 7, 11, 13], [h1, h2, i, j, k])[0]
            flag = long_to_bytes(flag)
            if b"flag" in flag:
                print(flag)
                exit()