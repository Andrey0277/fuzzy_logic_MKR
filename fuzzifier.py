import numpy as np


def fuzzification(crisp_values, input_lvs):
    """
    Returns the result of Fuzzification.
    """
    result = {}
    for index, crisp_value in enumerate(crisp_values):
        x_curr = np.argmax(input_lvs[index]['U'] >= crisp_value)
        result[index] = {}
        for term, mfs in input_lvs[index]['terms'].items():
            if mfs[x_curr] > 0:
                result[index][term] = mfs[x_curr]

    return result






