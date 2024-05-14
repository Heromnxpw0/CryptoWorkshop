from pwn import *
from Crypto.Util.number import *

conn = remote("95.111.237.98", 19824)
num = 0

while True:
    conn.recvuntil("Known >")

    conn.sendline(str(num))

    conn.recvuntil("a >")

    conn.sendline(str(2**500))

    response = conn.recvline().decode().strip()

    new_num = int(response)

    num += new_num

    print(response)

    if b"flag" in long_to_bytes(num):
        print("\nFlag found:", long_to_bytes(num))
        break

