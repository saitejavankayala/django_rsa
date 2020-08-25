import base64

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

pub_key = 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKINHuAQLOoINrgX9B9e5Z1y7L1ra6l9NbPvysyCYNVgjBsz4oo87ManzcJ2GacCzHTHf6zNSEwpY5YcnnKgXvsCAwEAAQ== '
priv_key = 'MIIBVwIBADANBgkqhkiG9w0BAQEFAASCAUEwggE9AgEAAkEAog0e4BAs6gg2uBf0H17lnXLsvWtrqX01s' \
           '+/KzIJg1WCMGzPiijzsxqfNwnYZpwLMdMd/rM1ITCljlhyecqBe+wIDAQABAkEAlEp1aozizPbfO++PkfWBIWe9hEj8qIjPz' \
           '+0rI6JbgmX2MfesvRYi/OreKOrra4gR9bZGFpCLISSmoZzVHpxPYQIhANSgMY9zl2OGK' \
           '+lIrYEEwZ8445lXlEskfjj0dmGaQE5vAiEAwxvPXL/cbkcrVpp+dOuXouM83AQoeHGV7TitQsFi/jUCIQDOlAkyv3JxXnUhRNxVgoJ' \
           '/qKzwWbeZPg5oVZMChvQ9fwIhAJ+drbv0HjJ9uL/F7nRalJgmjRB1umImkoAaoOv+56yNAiEApo2JwQuYrqsCZJPN7vZ21z5+WLj3Fo6pu' \
           '+zxEsusNes= '


def new_keys(key_size):
    random_generator = Random.new().read
    key = RSA.generate(key_size, random_generator)
    private, public = key, key.publickey()
    return public, private


def import_key(externKey):
    return RSA.importKey(externKey)


def export_private_key(private_key):
    with open("private_key", "wb") as f:
        f.write(private_key.exportKey())


def export_public_key(public_key):
    with open("public_key", "wb") as f:
        f.write(public_key.exportKey())


def getpublickey(priv_key):
    return priv_key.publickey()


def encrypt_chi(plain_text):
    cipher_text = pub_key.encrypt(plain_text, 32)[0]
    b64cipher = base64.b64encode(cipher_text)
    return b64cipher


def encrypt(message):
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(message)


def decrypt(ciphertext):
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.decrypt(ciphertext)


def verify_data(data, priv_key, ciphertext):
    return decrypt(ciphertext, priv_key) == data
