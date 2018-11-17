def str_xor(s1, s2):
    """
    Return the xor of two strings. It is assumed the two strings have
    the same length.

    :type s1: str
    :type s2: str
    :return: string
    """
    r = ""

    for c1, c2 in zip(s1, s2):
        r += chr(ord(c1) ^ ord(c2))

    return r


def hmac(key, m, hash_infos):
    """
    Hash-based message authentication code

    :param key: Key to use
    :type key: int
    :param m: message
    :type m: str
    :param hash_infos: tuple of a hash function and its block size
    :type hash_infos: 2D tuple, whose second member is an int
    :return: hex string
    """
    hash_func, block_size = hash_infos

    if len(key) > block_size:
        key = hash_func(key)

    if len(key) < block_size:
        key = key + '0' * (block_size - len(key))

    # Outer padded key
    opad = str_xor(key, '0x5C' * block_size)

    # Inner padded key
    ipad = str_xor(key, '0x36' * block_size)

    h1 = str_xor(key, opad)
    h2 = hash_func(str_xor(key, ipad) + m)

    return hash_func(h1 + h2)
