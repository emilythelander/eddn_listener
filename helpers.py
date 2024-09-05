def get_faction_happiness(band):
    match band:
        case "$faction_happinessband1;":
            return "Elated"
        case "$faction_happinessband2;":
            return "Happy"
        case "$faction_happinessband3;":
            return "Discontented"
        case "$faction_happinessband4;":
            return "Unhappy"
        case "$faction_happinessband5;":
            return "Despondent"
        case _:
            return "None"


def get_state(state):
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


def get_allegiance(power):
    match power:
        case "alliance":
            return "Alliance"
        case "empire":
            return "Empire"
        case "federation":
            return "Federation"
        case "independent":
            return "Independent"
        case "none":
            return "None"
        case "$pirate":
            return "Pirate"
        case "pilotsfederation":
            return "Pilots Federation"
        case "thargoid":
            return "Thargoid"
        case "guardian":
            return "Guardian"
        case _:
            return "None"


def get_government(gov):
    match gov:
        case "$government_anarchy;":
            return "Anarchy"
        case "$government_communism;":
            return "Communism"
        case "$government_confederacy;":
            return "Confederacy"
        case "$government_cooperative;":
            return "Cooperative"
        case "$government_corporate;":
            return "Corporate"
        case "$government_democracy;":
            return "Democracy"
        case "$government_dictatorship;":
            return "Dictatorship"
        case "$government_feudal;":
            return "Feudal"
        case "$government_imperial;":
            return "Imperial"
        case "$government_none;":
            return "None"
        case "$government_patronage;":
            return "Patronage"
        case "$government_prisoncolony;":
            return "Prison Colony"
        case "$government_theocracy;":
            return "Theocracy"
        case "$government_engineer;":
            return "Workshop"
        case _:
            return "None"


def get_security(sec):
    match sec:
        case "$galaxy_map_info_state_anarchy;":
            return "Anarchy"
        case "$galaxy_map_info_state_lawless;":
            return "Lawless"
        case "$system_security_high;":
            return "High"
        case "$system_security_low;":
            return "Low"
        case "$system_security_medium;":
            return "Medium"
        case _:
            return "None"


def get_station_type(station):
    match station:
        case "coriolis":
            return "Coriolis Starport"
        case "coriolis_starport":
            return "Coriolis Starport"
        case "bernal":
            return "Ocellus Starport"
        case "ocellus starport":
            return "Ocellus Starport"
        case "orbis":
            return "Orbis Starport"
        case "orbis starport":
            return "Orbis Starport"
        case "outpost":
            return "Outpost"
        case "civilian outpost":
            return "Outpost"
        case "commercial outpost":
            return "Outpost"
        case "industrial outpost":
            return "Outpost"
        case "military outpost":
            return "Outpost"
        case "mining outpost":
            return "Outpost"
        case "scientific outpost":
            return "Outpost"
        case "surfacestation":
            return "Planetary Outpost"
        case "crateroutpost":
            return "Planetary Outpost"
        case "planetary port":
            return "Planetary Port"
        case "craterport":
            return "Planetary Port"
        case "asteroidbase":
            return "Asteroid Base"
        case "megaship":
            return "Megaship"
        case _:
            return "None or Other"
