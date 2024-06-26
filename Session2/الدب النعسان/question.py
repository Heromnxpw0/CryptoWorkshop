from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import bytes_to_long
from secret import FLAG


# Generate a new RSA key pair
key = RSA.generate(2048)
n = key.n
e = key.e
d = key.d
p = key.p
q = key.q
phi = (p-1)*(q-1)

ct = pow(bytes_to_long(FLAG), e, n)

print(f"phi = {phi}")
print(f"ct = {ct}")
print(f"p = {p}")
