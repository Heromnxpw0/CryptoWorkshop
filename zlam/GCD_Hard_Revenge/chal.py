from Crypto.Util.number import *
from secret import flag
real_flag = flag
flag = getPrime(64)

for i in range(16):
    a = int(input("a >").strip())
    b = int(input("b >").strip())
    if a == 0 or b == 0:
        print("yeah nice try ziadstr checked it this time")
        exit()
    print(GCD(a, flag - b))

x = int(input("Give me a guess >"))
if x == flag:
    print(real_flag)
# What is the flag?