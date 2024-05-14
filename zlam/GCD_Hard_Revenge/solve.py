from sympy.ntheory.modular import crt
from Crypto.Util.number import *
from pwn import *
context.log_level = 'DEBUG'

url = "95.111.237.98"
port = 19829

a = 1
for i in range(1, 101):
    a *= i
r = remote(url, port)

ans = []
mods = []

for i in range(1, 17):
    r.recvuntil("a >")
    r.sendline(str(a))
    r.recvuntil("b >")
    r.sendline(str(i))
    b = r.recvline().decode().strip()
    mods.append(int(b))
    ans.append(int(i))
    
x = crt(mods, ans)[0]
r.recvuntil(">")
r.sendline(str(x))

r.interactive()