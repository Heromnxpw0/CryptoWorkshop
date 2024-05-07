from Crypto.Util.number import *

e = 65537
p = getPrime(512)
q = getPrime(512)
n = p*q

flag = b'flag{REDACTED}'

c = pow(bytes_to_long(flag), e, n)
with open('Workshop/BabyRSA/out.txt','w') as f:
    f.write(f'p = {p} \n')
    f.write(f'q = {q} \n')
    f.write(f'c = {c} \n')
    f.write(f'e = {e} \n')
