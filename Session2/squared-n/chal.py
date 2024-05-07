from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

flag = b"flag{REDACTED}"

p = getPrime(1024)
n = p * p
e = 65537
c = pow(bytes_to_long(flag), e, n)

with open("FactoredN/out.txt", "w") as f:
    f.write(f"n = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"c = {c}\n")
