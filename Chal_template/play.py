from Crypto.Util.number import long_to_bytes, bytes_to_long, getStrongPrime, inverse

class RSA:
    def __init__(self, bit_length=1024):
        self.e = 65537
        self.p = getStrongPrime(bit_length)
        self.q = getStrongPrime(bit_length)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.d = inverse(self.e, self.phi)

    def encrypt(self, plaintext):
        pt_long = bytes_to_long(plaintext)
        ct = pow(pt_long, self.e, self.n)
        return ct, self.e, self.n

    def decrypt(self, ciphertext):
        plaintext = pow(ciphertext, self.d, self.n)
        return long_to_bytes(plaintext)


    def decrypt(self, ciphertext):
        pt = pow(ciphertext, self.d, self.n)
        return pt

    # def special_decrypt(self, ciphertext):
    #     cb = pow(2, self.e, self.n) * ciphertext % self.n
    #     cbd = int(pow(cb, self.d, self.n) // 2)
    #     return long_to_bytes(cbd)
def printGalaga():
	print('┌──────────────────────────────────────────┐\n')
	print('│  ┌────────────────────────────────────┐  │\n')
	print('│  │  ╔══════════════════════════════╗  │  │\n')
	print('│  │  ║           GALAGA             ║  │  │\n')
	print('│  │  ╚══════════════════════════════╝  │  │\n')
	print('│  │     /\\\       /\\\     /\\\  /\\\     │  │\n')
	print('│  │    /==\\\     /==\\\   /========\\\   │  │\n')
	print('│  │     \\\/       \\\/     \\\/  \\\/     │  │\n')
	print('│  │                                    │  │\n')
	print('│  │    Score: 00000  Lives: ***        │  │\n')
	print('│  └────────────────────────────────────┘  │\n')
	print('│                                          │\n')
	print('└──────────────────────────────────────────┘\n')

if __name__ == '__main__':
	flag = open('flag.txt', 'rb').read()

	rsa = RSA()
	Flagct, Flage, Flagn = rsa.encrypt(flag)
	printGalaga()
	while True:
		print('\033[1mWelcome to the Galaga, something is wrong i dont know how you can win this:\n1-Encrypt\n2-Decrypt\n3-Get flag\n4-Exit\033[0m')
		option = int(input('> '))
		if option == 1:
			print("Give me the plaintext:")
			pt = bytes(input('> ').encode())
			ct, e, n = rsa.encrypt(pt)
			print(f"ct = {ct}")
			print(f"e = {e}")
			print(f"n = {n}")
		if option == 2:
			print("Give me the ciphertext:")
			ct = int(input('> '))
			if ct == Flagct:
				print("Nice try!! go play somewhere else...")
				exit()
			else:
				pt = rsa.decrypt(ct)
				print(f"btyes_to_long(pt) = {pt}")
		if option == 3:
			print(f"ct = {Flagct}")
			print(f"e = {Flage}")
			print(f"n = {Flagn}")
		if option == 4:
			exit()