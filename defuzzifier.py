import numpy as np
import sys


def defuzzification(x, mf, defuzz_type='cog'):
    method = getattr(sys.modules[__name__], f'__{defuzz_type}', None)
    return method(x, mf) if method else method


def __cog(x, mf) -> float:
    """
    Returns the center of gravity of the fuzzy set along the x-axis.
    """

    if len(x) != len(mf):
        raise ValueError("The number of items in 'x' does not math with 'mfs'")

    return np.sum(x * mf) / np.sum(mf)


def __fom(x, mf) -> float:
    """
    Returns the First of Maximum of the fuzzy set along the x-axis.
    """

    if len(x) != len(mf):
        raise ValueError("The number of items in 'x' does not math with 'mfs'")

    return x[np.argmax(mf)]


def __lom(x, mf) -> float:
    """
    Returns the Last of Maximum of the fuzzy set along the x-axis.
    """

    if len(x) != len(mf):
        raise ValueError("The number of items in 'x' does not math with 'mfs'")

    y = np.where(mf == mf.max())
    return x[y[0][-1]]


def __mom(x, mf) -> float:
    """
    Returns the Middle of Maximum of the fuzzy set along the x-axis.
    """

    if len(x) != len(mf):
        raise ValueError("The number of items in 'x' does not math with 'mfs'")

    y = np.where(mf == mf.max())
    return (x[y[0][0]] + x[y[0][-1]]) / 2


def jaccard_measure(x_mf, y_mf) -> float:
    min_mf = (min(a, b) for a, b in zip(x_mf, y_mf))
    max_mf = (max(a, b) for a, b in zip(x_mf, y_mf))

    return sum(min_mf) / sum(max_mf)