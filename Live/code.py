from Crypto.Util.number import *

# this is a bytes object, we can use bytes to long to turn it into a number and long to bytes to reverse it
p1 = b"Help me pwease"


long = bytes_to_long(p1)


p2 = long_to_bytes(long)

print(f"{p1} = {long} = {p2}")

# the way this works is by using big endian notation (google at your own risk)

# python has a great pow function, it can be used to do variace things

print(pow(2, 3)) # powers normally
print(pow(4, 5, 12)) # powers with a mod
print(4 * pow(4, -1, 13) % 13) # Calculate mod inverse


# you can also use python gcd or the one in pycryptodome

print(GCD(11111, 55555))

# submit this flag flag{Let_the_games_begin}