import itertools
import numpy as np
import fuzzy_operators
import membership_functions
import fuzzifier
import defuzzifier


def preprocessing(input_lvs, output_lv):
    # Creation of thr Universe
    for item in input_lvs:
        item['U'] = np.arange(*item['X'])
    output_lv['U'] = np.arange(*output_lv['X'])

    # Creation of the MFs
    for lv in input_lvs:
        for key, value in lv['terms'].items():
            mf, *params = value
            lv['terms'][key] = getattr(membership_functions, mf)(lv['U'], *params)

    for key, value in output_lv['terms'].items():
        mf, *params = value
        output_lv['terms'][key] = getattr(membership_functions, mf)(output_lv['U'], *params)


def activated_rules(fuzzy_values, rule_base):
    terms = (item.keys() for item in fuzzy_values.values())
    antecedents = tuple(itertools.product(*terms))
    return [rule for rule in rule_base if rule[0] in antecedents]


def implication(fuzzy_values, activated_rules, output_lv):
    result = []
    for rule in activated_rules:
        antecedent, consequent = rule
        mfs = (fuzzy_values[index][term] for index, term in enumerate(antecedent))
        tmp = fuzzy_operators.fuzzy_min(output_lv['terms'][consequent], min(mfs))
        result.append(tmp)
    return result


def aggregation(*fuzzy_sets):
    return fuzzy_operators.fuzzy_union(*fuzzy_sets)


def process(input_lvs, output_lv, rule_base, crisp_values):
    fuzzy_values = fuzzifier.fuzzification(crisp_values, input_lvs)

    rules = activated_rules(fuzzy_values, rule_base)
    implication_fuzzy_sets = implication(fuzzy_values, rules, output_lv)
    result_fuzzy_set = aggregation(*implication_fuzzy_sets)

    crisp_result = defuzzifier.defuzzification(output_lv['U'], result_fuzzy_set, 'cog')
    word_result = []
    for term, mf in output_lv['terms'].items():
        sm = defuzzifier.jaccard_measure(result_fuzzy_set, mf)
        word_result.append((term, sm))
    word_result = max(word_result, key=lambda item: item[1])

    return crisp_result, word_result[0]

