from Crypto.Util.number import *
from secret import flag, message

print(message)

flag = bytes_to_long(flag)

for i in range(len(bin(flag)) - 2):
    known = int(input("Known >").strip())
    g = int(input("a >").strip())
    assert g > 0
    print(GCD(g, flag - known))
    
# This probably a bad idea, but meh