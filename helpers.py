def get_faction_happiness(band):
    if band == "$faction_happinessband1;":
        parsed_band = "Elated"
    elif band == "$faction_happinessband2;":
        parsed_band = "Happy"
    elif band == "$faction_happinessband3;":
        parsed_band = "Discontented"
    elif band == "$faction_happinessband4;":
        parsed_band = "Unhappy"
    elif band == "$faction_happinessband5;":
        parsed_band = "Despondent"
    else:
        parsed_band = "None"
    return parsed_band
