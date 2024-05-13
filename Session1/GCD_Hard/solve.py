from secret import flag
from Crypto.Util.number import *


print(len(bin(bytes_to_long(flag))) - 2)