from Crypto.Util.number import getPrime,getRandomInteger,bytes_to_long
from secret import flag 
p = getPrime(512)

random = getRandomInteger(512) % p
coeff = pow(random,-1,p)
flag = bytes_to_long(flag)
ct = coeff * flag % p
print(f'p = {p}')
print(f'ct = {ct}')
print(f'random = {random}')
