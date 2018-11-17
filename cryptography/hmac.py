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

    if key > block_size:
        key = hash_func(key)

    if key < block_size:
        key = key + '0' * (block_size - len(key))

    # Outer padded key
    opad = key ^ '0x5C' * block_size
    opad = []

    # Inner padded key
    ipad = key ^ '0x36' * block_size

    return hash_func(key ^ opad + h((key ^ ipad) + m))
