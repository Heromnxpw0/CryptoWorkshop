from Crypto.Util.number import *
from secret import flag

flag = bytes_to_long(flag)

for i in range(16):
    a = int(input("a >").strip())
    b = int(input("b >").strip())
    print(GCD(a, flag - b))


# What is the flag?