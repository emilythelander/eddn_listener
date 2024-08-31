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


def get_faction_states(state):
    match state:
        case "none":
            return "None"
        case "boom":
            return "Boom"
        case "bust":
            return "Bust"
        case "civilunrest":
            return "Civil Unrest"
        case "civilwar":
            return "Civil War"
        case "civilliberty":
            return "Civil Liberty"
        case "election":
            return "Election"
        case "expansion":
            return "Expansion"
        case "famine":
            return "Famine"
        case "investment":
            return "Investment"
        case "lockdown":
            return "Lockdown"
        case "outbreak":
            return "Outbreak"
        case "pirateattack":
            return "Pirate Attack"
        case "retreat":
            return "Retreat"
        case "war":
            return "War"
        case "blight":
            return "Blight"
        case "drought":
            return "Drought"
        case "infrastructurefailure":
            return "Infrastructure Failure"
        case "naturaldisaster":
            return "Natural Disaster"
        case "publicholiday":
            return "Public Holiday"
        case "terrorism":
            return "Terrorist Attack"
        case _:
            return "None"


def get_conflict_type(type):
    match type:
        case "war":
            return "War"
        case "civilwar":
            return "Civil War"
        case "election":
            return "Election"
        case _:
            return "None"


def get_economy(econ):
    match econ:
        case "$economy_agri;":
            return "Agriculture"
        case "$economy_colony;":
            return "Colony"
        case "$economy_extraction;":
            return "Extraction"
        case "$economy_hightech;":
            return "High Tech"
        case "$economy_industrial;":
            return "Industrial"
        case "$economy_military;":
            return "Military"
        case "$economy_none;":
            return "None"
        case "$economy_refinery;":
            return "Refinery"
        case "$economy_service;":
            return "Service"
        case "$economy_terraforming;":
            return "Terraforming"
        case "$economy_tourism;":
            return "Tourism"
        case "$economy_repair;":
            return "Repair"
        case "$economy_rescue;":
            return "Rescue"
        case "$economy_damaged;":
            return "Damaged"
        case _:
            return "None"
