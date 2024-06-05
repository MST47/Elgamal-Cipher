from Cryptodome.Util.number import getPrime, getRandomRange
from Cryptodome.PublicKey import ElGamal

                   #----------  Generation of Keys ----------------

# Generate a 128-bit prime number
p = getPrime(128)

# Generate a private key
x = getRandomRange(1, p-2)

# Generate a public key
g = 2                         # we use a fixed generator
y = pow(g, x, p)
public_key = ElGamal.construct((p, g, y))
# Generate a Private Key
private_key = (p, x)

# -------------------------- Encryption Algorithms----------------------

# Encrypt a message using the public key
message = b'Hello, World!'
plaintext = int.from_bytes(message, 'big')

# Generate a random number k
k = getRandomRange(1, p-2)

# Compute the ciphertext
c1 = pow(g, k, p)
c2 = plaintext * pow(y, k, p) % p
ciphertext = (c1, c2)

# -------------------------- Decryption Algorithms----------------------

# Decrypt the ciphertext using the private key
c1, c2 = ciphertext

plaintext = c2 * pow(c1, p-1-x, p) % p

# Convert the plaintext back to bytes
message = plaintext.to_bytes((plaintext.bit_length() + 7) // 8, 'big')


print(ciphertext)
print(message.decode())



