from Crypto.Util.number import *
from sympy.ntheory.modular import crt
import gmpy2

with open("zlam\Repeated_message\out.txt", "r") as f:
    ns = eval(f.readline().split(" = ")[1])
    e = eval(f.readline().split(" = ")[1])
    cts = eval(f.readline().split(" = ")[1])
    

ct = crt(ns, cts)[0]

m = gmpy2.iroot(ct, e)[0]

print(long_to_bytes(m))