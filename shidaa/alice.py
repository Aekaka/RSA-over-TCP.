import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def alice():
    # Generate a 1024-bit RSA key pair
    keyPair = RSA.generate(1024)
    pubKey = keyPair.publickey()
    print(f"Alice's public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
    print(f"Alice's private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")

    # Start a server to send the public key and receive the ciphertext
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9500))
    server.listen(1)
    while True:
        client, addr = server.accept()
        if client:
            client.send(pubKey.exportKey())
            ciphertext = client.recv(1024)
            print("Ciphertext:", binascii.hexlify(ciphertext))

            # Decrypt the ciphertext with the private key
            decryptor = PKCS1_OAEP.new(keyPair)
            decrypted = decryptor.decrypt(ciphertext)
            print('Decrypted:', decrypted.decode('utf-8'))
