from Crypto.Util.number import *
from secret import flag

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 65537


ct = []
for letter in flag:
    ct.append(pow(ord(letter), e, n))
    
    
with open("out.txt", "w") as f:
    f.write(str(n) + "\n")
    f.write(str(e) + "\n")
    f.write(str(ct) + "\n")