from Crypto.Util.number import *

with open(r"Session1\factorwithmod\out.txt", "r") as f:
    n = int(f.readline().strip().split(" = ")[1])
    factors = [int(x.strip().split(" = ")[1]) % n for x in f.readlines()]

flag = 1
for factor in factors:
    flag *= factor
    
print(long_to_bytes(flag))