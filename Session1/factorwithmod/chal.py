from Crypto.Util.number import getPrime,getRandomInteger,bytes_to_long
from factordb.factordb import FactorDB
from secret import flag

num = bytes_to_long(flag)
f = FactorDB(num)
f.connect()
factors = f.get_factor_list()

p = getPrime(512)
q = getPrime(512)
n = p*q

print(f"n = {n}")
for factor in factors :
    factor = getRandomInteger(512) * n + factor
    print(f"factor = {factor}")