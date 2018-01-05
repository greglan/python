from math import log, cos, sin, pi


def deg_to_rad(d):
    return pi * d / 180


def rad_to_deg(d):
    return d * 180 / pi


def kmh_to_ms(v):
    return v / 3.6


def int_to_dB(x):
    return 10 * log(x, 10)


def dB_to_int(x):
    return 10 ** (x / 10)


def int_to_dBm(x):
    return 10 * log(x * 10 ** 3, 10)


def dBm_to_int(x):
    return 10 ** (x / 10 - 3)


def doppler(f, v, c):
    return abs(f - f / (1 - v / c))


c = 3 * 10 ** 8
