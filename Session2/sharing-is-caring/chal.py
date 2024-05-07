from Crypto.Util.number import *

flag= b"flag{REDACTED}"

flag1 = flag[:len(flag)//2]
flag2 = flag[len(flag)//2:]

p = getPrime(1024)
q_1 = getPrime(1024)
q_2 = getPrime(1024)
n_1 = p * q_1
n_2 = p * q_2
e = 65537
c_1 = pow(bytes_to_long(flag1), e, n_1)
c_2 = pow(bytes_to_long(flag2), e, n_2)

with open("sharing-is-caring/out.txt", "w") as f:
    f.write(f"n_1 = {n_1}\n")
    f.write(f"n_2 = {n_2}\n")
    f.write(f"e = {e}\n")
    f.write(f"c_1 = {c_1}\n")
    f.write(f"c_2 = {c_2}\n")
