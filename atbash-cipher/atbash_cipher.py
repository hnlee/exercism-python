from string import maketrans, ascii_lowercase, whitespace, punctuation

def decode(message):
    cipher = maketrans(ascii_lowercase, ascii_lowercase[::-1])
    decoded = message.translate(cipher, whitespace)
    return decoded

def encode(message):
    cipher = maketrans(ascii_lowercase, ascii_lowercase[::-1])
    encoded = message.lower().translate(cipher, whitespace + punctuation)
    return ' '.join(list(encoded[i:i+5]
                         for i in range(0, len(encoded), 5)))
