def ksa(key):
    """
    Key Scheduling Algorithm
    :return: S
    """
    key_length = len(key)
    if 1 > key_length or key_length > 256:
        raise ValueError("Invalid key length")

    S = [i for i in range(256)]  # Identity permutation

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # Swap values


def prga(S, n):
    """
    Pseudo-random generation algorithm
    :return: keystream
    """

    keystream = []
    i = 0
    j = 0

    while n != 0:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Swap values
        K = S[(S[i] + S[j]) % 256]

        keystream.append[K]

        n -= 1

    return keystream


def rc4(key, plaintext):
    n = len(plaintext)
    S = ksa(key)
    keystream = prga(S, n)
    ciphertext = ""

    for i in range(n):
        ciphertext = keystream[i] ^ plaintext[i]

    return ciphertext
