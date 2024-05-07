from Crypto.Util.number import *
from secret import flag

p = getPrime(512)

phi = p - 1
r = getRandomInteger(512)
print(f"hint: {phi}")
a = input("Enter a >")
a = int(a.strip())

if a == phi or a < 1:
    print("Nope")
    exit()
    
if pow(r, a + 1, p) == r:
    print("You win, here is your flag: ", flag)
else:
    print("Ask H04X for the asnwer")