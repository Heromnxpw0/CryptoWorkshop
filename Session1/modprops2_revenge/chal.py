from Crypto.Util.number import getPrime,getRandomInteger,bytes_to_long
from factordb.factordb import FactorDB
from secret import flag
num = bytes_to_long(flag)
f = FactorDB(num)
f.connect()
factors = f.get_factor_list()

n = getPrime(1024)

print(f"n = {n}")
phi = n - 1
edited_factors = []
coeffs = []
for factor in factors:
    coeff = getRandomInteger(128)
    factor = getRandomInteger(512) * n - coeff * factor
    coeffs.append(coeff)
    edited_factors.append(factor)
print(f'factors = {edited_factors}')
print(f'coeffs = {coeffs}')
