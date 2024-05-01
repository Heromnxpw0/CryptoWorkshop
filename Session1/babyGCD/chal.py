from Crypto.Util.number import getRandomInteger,bytes_to_long
from secret import flag
flag = bytes_to_long(flag)

rand1 = getRandomInteger(128)

rand2 = getRandomInteger(128)

print("val1 = ",rand1*flag)
print("val2 = ",rand2*flag)
