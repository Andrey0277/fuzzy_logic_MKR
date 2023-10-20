input_lvs = [
    {  # 0\100 рівень води
        "X": (0, 101, 1),
        "name": "water_level",
        "terms": {
            "low": ("trapmf", 0, 0, 18, 40),
            "medium": ("trapmf", 20, 40, 50, 70),
            "high": ("trapmf", 60, 70, 101, 101),
        },
    },
    # Winter Spring Summer autumn
    {
        "X": (0, 12, 1),
        "name": "season",
        "terms": {
            "Winter": ("trapmf", 0, 0, 1, 3),
            "Spring": ("trapmf", 1, 3, 4, 5),
            "Summer": ("trapmf", 4, 5, 6, 8),
            "Autumn": ("trapmf", 7, 9, 10, 11),
        },
    },
    # 0-50 градусів
    {
        "X": (0, 50.01, 0.01),
        "name": "average_air_temperature",
        "terms": {
            "low": ("trapmf", 0, 0, 12, 18),
            "medium": ("trapmf", 14, 20, 25, 30),
            "high": ("trapmf", 25, 30, 51, 51),
        },
    },
]

output_lv = {
    "X": (0, 1, 0.01),
    "name": "Attractive level",
    "terms": {
        "no_need": ("trapmf", 0, 0, 0.3, 0.5),
        "not_critical": ("trimf", 0.3, 0.7, 0.8),
        "need": ("trapmf", 0.7, 0.8, 1.1, 1.1),
    },
}


rule_base = [
    (("low", "Winter", "low"), "need"),
    (("low", "Winter", "medium"), "need"),
    (("low", "Winter", "high"), "need"),
    (("low", "Spring", "low"), "need"),
    (("low", "Spring", "medium"), "need"),
    (("low", "Spring", "high"), "need"),
    (("low", "Summer", "low"), "need"),
    (("low", "Summer", "medium"), "need"),
    (("low", "Summer", "high"), "need"),
    (("low", "Autumn", "low"), "need"),
    (("low", "Autumn", "medium"), "need"),
    (("low", "Autumn", "high"), "need"),
    (("medium", "Winter", "low"), "not_critical"),
    (("medium", "Winter", "medium"), "not_critical"),
    (("medium", "Winter", "high"), "need"),
    (("medium", "Spring", "low"), "not_critical"),
    (("medium", "Spring", "medium"), "need"),
    (("medium", "Spring", "high"), "need"),
    (("medium", "Summer", "low"), "need"),
    (("medium", "Summer", "medium"), "need"),
    (("medium", "Summer", "high"), "need"),
    (("medium", "Autumn", "low"), "need"),
    (("medium", "Autumn", "medium"), "need"),
    (("medium", "Autumn", "high"), "need"),
    (("high", "Winter", "low"), "no_need"),
    (("high", "Winter", "medium"), "no_need"),
    (("high", "Winter", "high"), "not_critical"),
    (("high", "Spring", "low"), "no_need"),
    (("high", "Spring", "medium"), "not_critical"),
    (("high", "Spring", "high"), "not_critical"),
    (("high", "Summer", "low"), "not_critical"),
    (("high", "Summer", "medium"), "not_critical"),
    (("high", "Summer", "high"), "need"),
    (("high", "Autumn", "low"), "not_critical"),
    (("high", "Autumn", "medium"), "not_critical"),
    (("high", "Autumn", "high"), "need"),
]
