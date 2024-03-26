import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def bob():
    # Connect to Alice's server to receive the public key
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9500))
    pubKey = RSA.importKey(client.recv(1024))

    # Encrypt a message using Alice's public key
    message = b'Hello Alice!'
    encryptor = PKCS1_OAEP.new(pubKey)
    ciphertext = encryptor.encrypt(message)
    print("Ciphertext:", binascii.hexlify(ciphertext))

    # Send the ciphertext back to Alice
    client.send(ciphertext)
