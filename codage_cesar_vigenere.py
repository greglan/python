alphabet = []


def decalage(X, Y):
    """
    Returns letter X shifted of Y
    :param X:
    :param Y:
    :return:
    """
    # x + y = k*26 + r
    return chr(((ord(X) + ord(Y) - 64 - 64) % 26) + 64);


def codage(word, key):
    p = len(key);
    n = len(word);
    s = "";
    for i in range(0, n):
        s += decalage(word[i], key[i % p]);
    return s;


def decodage(word, key):
    p = len(key);
    n = len(word);
    s = "";
    for i in range(0, n):
        s += decalage2(word[i], key[i % p]);
    return s;


def indices(x, phrase):
    n = len(phrase)
    l = []
    for i in range(n):
        if phrase[i] == x:
            l.append(i)
    return l
