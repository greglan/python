def compress(s):
    """
    Compress a string by replacing n contiguous characters c by cn
    :param s: string to compress
    :type s: str
    :return: str
    """
    n = len(s)
    i = 0
    j = 1
    compressed_str = ""

    while j < len(s):
        if s[j] == s[i]:
            j += 1
        else:
            compressed_str += s[i] + str(j-i)
            i = j
            j += 1

    compressed_str += s[i] + str(j - i)

    return compressed_str
