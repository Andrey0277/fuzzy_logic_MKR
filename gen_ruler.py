import itertools

from model import input_lvs

data = dict()
j = []
for value in input_lvs:
    data[value["name"]] = [t for t in value["terms"]]
    j.append(value["name"])


print(j)
# water_level season average_air_temperature
# no_need not_critical  need

value = {
    "water_level": lambda x: -2 * x,  # чим більше вод тим менше неохідність в неї
    "season": lambda x: x if x < 3 else 5 - x,  # спочатку стає жарко потім холоднішає
    "average_air_temperature": lambda x: x,  # випаровування
}


rez = []
rez2 = []
for tupl in tuple(itertools.product(*[data[i] for i in data])):
    t = 0
    for index, param in enumerate(data):
        t += value[param](data[param].index(tupl[index]))
    t += 5
    rez2.append(t)
    t2 = (tupl, "no_need")
    if t > 2:
        t2 = (tupl, "not_critical")
    if t > 4:
        t2 = (tupl, "need")

    rez.append((t2))


print(rez)
[
    (("low", "Winter", "low"), "high"),
    (("low", "Winter", "medium"), "high"),
    (("low", "Winter", "high"), "high"),
    (("low", "Spring", "low"), "high"),
    (("low", "Spring", "medium"), "high"),
    (("low", "Spring", "high"), "high"),
    (("low", "Summer", "low"), "high"),
    (("low", "Summer", "medium"), "high"),
    (("low", "Summer", "high"), "high"),
    (("low", "Autumn", "low"), "high"),
    (("low", "Autumn", "medium"), "high"),
    (("low", "Autumn", "high"), "high"),
    (("medium", "Winter", "low"), "medium"),
    (("medium", "Winter", "medium"), "medium"),
    (("medium", "Winter", "high"), "high"),
    (("medium", "Spring", "low"), "medium"),
    (("medium", "Spring", "medium"), "high"),
    (("medium", "Spring", "high"), "high"),
    (("medium", "Summer", "low"), "high"),
    (("medium", "Summer", "medium"), "high"),
    (("medium", "Summer", "high"), "high"),
    (("medium", "Autumn", "low"), "high"),
    (("medium", "Autumn", "medium"), "high"),
    (("medium", "Autumn", "high"), "high"),
    (("high", "Winter", "low"), "low"),
    (("high", "Winter", "medium"), "low"),
    (("high", "Winter", "high"), "medium"),
    (("high", "Spring", "low"), "low"),
    (("high", "Spring", "medium"), "medium"),
    (("high", "Spring", "high"), "medium"),
    (("high", "Summer", "low"), "medium"),
    (("high", "Summer", "medium"), "medium"),
    (("high", "Summer", "high"), "high"),
    (("high", "Autumn", "low"), "medium"),
    (("high", "Autumn", "medium"), "medium"),
    (("high", "Autumn", "high"), "high"),
]
