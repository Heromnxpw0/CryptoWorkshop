from Crypto.Util.number import *

def get_RSA_params():
    p = getPrime(1024)
    q = getPrime(1024)
    N = p*q
    phi = (p-1)*(q-1)
    while True:
        d = getPrime(256)
        e = pow(d,-1,phi)
        if e.bit_length() == N.bit_length():
            break
    return N,e

n,e = get_RSA_params()
flag = b'flag{REDACTED}'
c = pow(bytes_to_long(flag), e, n)
with open('large-e/out.txt','w') as f:
    f.write(f'n = {n} \n')
    f.write(f'c = {c} \n')
    f.write(f'e = {e} \n')
