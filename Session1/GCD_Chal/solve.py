from Crypto.Util.number import *

with open("Session1\GCD_Chal\out.txt", "r") as f:
    hint = eval(f.readline().strip().split(" = ")[1])
    ct = int(f.readline().strip().split(" = ")[1])
    
for h in hint:
    ct = ct // GCD(h, ct)
print(long_to_bytes(ct))