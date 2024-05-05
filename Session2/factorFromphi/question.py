from Crypto.Util.number import *
from secret import FLAG
from random import randint

print("""
I need your help solving my 8th grade HW, recently we took the basics of factoring but i am really bad at it.
Can you help me please?
""")

p = getPrime(1024)
q = getPrime(1024)
if p < q:
    p, q = q, p
n = p * q
question = {"n" : hex(n)[2:]}
question["phi"] = hex((p - 1) * (q - 1))[2:]

print(question)

p_ = input("Enter p (hex):")
q_ = input("Enter q (hex):")
p_ = int(p_ ,16)
q_ = int(q_, 16)

if p_ != p or q_ != q:
    print("Guess you arent as smart as i thought you were :(")
    exit()
        
print("Good Job, my parents bought me a gift because of my high grade, here take this as a thanks.") 
print(FLAG)   