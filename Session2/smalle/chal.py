from Crypto.Util.number import *

e = 3
p = getPrime(512)
q = getPrime(512)
n = p*q

flag = b'flag{sm4ll_e_is_n0t_s3cur3}'
c = pow(bytes_to_long(flag), e, n)
with open('Workshop/Smalle/out.txt','w') as f:
    f.write(f'n = {n} \n')
    f.write(f'c = {c} \n')
    f.write(f'e = {e} \n')
