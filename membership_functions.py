import numpy as np


def __trapmf(x, a, b, c, d):
    if x < a:
        return 0.
    elif a <= x < b:
        return (x - a) / (b - a)
    elif b <= x <= c:
        return 1.
    elif c < x <= d:
        return (d - x) / (d - c)
    return 0.


def trapmf(x, a: float, b: float, c: float, d: float):
    iterable = (__trapmf(item, a, b, c, d) for item in x)
    mf = np.fromiter(iterable, float)
    return np.nan_to_num(mf)


def __trimf(x, a, b, c):
    if x < a:
        return 0.
    elif a <= x < b:
        return (x - a) / (b - a)
    elif x == b:
        return 1.
    elif b < x <= c:
        return (c - x) / (c - b)
    return 0.


def trimf(x, a: float, b: float, c: float):
    iterable = (__trimf(item, a, b, c) for item in x)
    mf = np.fromiter(iterable, float)
    return np.nan_to_num(mf)
