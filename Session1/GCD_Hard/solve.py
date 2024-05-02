import subprocess

proc = subprocess.Popen(['python', 'Session1\GCD_Hard\chal.py'], stdin=subprocess.PIPE, 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE,
                        bufsize=1,  # Line buffered
                        universal_newlines=True)

# Read the response
response = proc.stdout.read()
print(response)