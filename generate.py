from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import (
    X25519PrivateKey, X25519PublicKey
)

TRAINING_SIZE = 3000000
FILES = 100


file_number = 0
while file_number < FILES:
    questions = 0
    f = open('keys-3M-' + str(file_number), 'w')
    while questions < TRAINING_SIZE:
        private_key = X25519PrivateKey.generate()
        public_key = private_key.public_key()
        question = public_key.public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw)
        answer = private_key.private_bytes(serialization.Encoding.Raw, serialization.PrivateFormat.Raw,serialization.NoEncryption())
        print(question.hex(),answer.hex(), file=f)
        questions += 1
    f.close()
    file_number += 1
