import hashlib
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64
text = "Bitcoin price today"
hash_object = hashlib.sha256(text.encode())
print("SHA-256:", hash_object.hexdigest())
key = b'1234567890123456'
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(text.encode())
decipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = decipher.decrypt(ciphertext)
print("AES decrypted:", plaintext.decode())
key_pair = RSA.generate(2048)
message_hash = SHA256.new(text.encode())
signature = pkcs1_15.new(key_pair).sign(message_hash)
try:
    pkcs1_15.new(key_pair.publickey()).verify(message_hash, signature)
    print("RSA: signature confirmed")
except:
    print("RSA: signature not confirmed")
