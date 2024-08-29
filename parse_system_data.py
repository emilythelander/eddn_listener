import get_json_data as gjd
import time_functions as tf
import helpers as h


# Takes dictionary as input
def parse_system_data(json_dict):
    if type(json_dict) is not dict:
        gjd.write_error(
            "parse_system_data failed due to input object not being type dict. "
        )
        print(
            "Unable to parse JSON system data, input provided is not a dict object. See error file for more details."
        )
        return -1

    # Gets the system name and creates the initial dictionary to be used for output later on.
    # If the system name doesn't exist in the json file, we know that either it's a dead system
    # (i.e. Lanaest) or something is funky with the data and we can't continue.

    try:
        sys_name = json_dict["docs"][0]["name"]
    except Exception as e:
        with open("error.txt", "a") as errorfile:
            errorfile.write(
                "Data for system " f" either isn't present or has some other issue. {e}"
            )
        return -1

    final_dict = {"Name": sys_name}

    # Compare update date with last tick to see if the data is current or not
    last_update = tf.convert_tz(json_dict["docs"][0]["updated_at"])
    current = tf.is_current(last_update)
    final_dict.update({"Current": current})

    # Get other basic system information we'll always want
    allegiance = (json_dict["docs"][0]["allegiance"]).capitalize()
    final_dict.update({"Allegiance": allegiance})
    government = ((json_dict["docs"][0]["government"])[12:-1]).capitalize()
    final_dict.update({"Government": government})
    final_dict.update({"Population": json_dict["docs"][0]["population"]})
    prim_eco = ((json_dict["docs"][0]["primary_economy"])[9:-1]).capitalize()
    final_dict.update({"Primary Economy": prim_eco})
    sec_eco = ((json_dict["docs"][0]["secondary_economy"])[9:-1]).capitalize()
    final_dict.update({"Secondary Economy": sec_eco})
    security = ((json_dict["docs"][0]["security"])[17:-1]).capitalize()
    final_dict.update({"Security": security})
    state = (json_dict["docs"][0]["state"]).capitalize()
    final_dict.update({"System State": state})

    # Cycle through system factions, create new dictionary for faction influence data, sort by inf desc
    uns_fac_inf_dict = {}
    for doc in json_dict["docs"]:
        for faction in doc["factions"]:
            fac_name = faction.get("name")
            fac_inf = faction["faction_details"]["faction_presence"]["influence"]
            fac_inf = fac_inf * 100
            uns_fac_inf_dict.update({fac_name: fac_inf})

    sor_fac_inf_dict = sorted(
        uns_fac_inf_dict.items(), key=lambda x: x[1], reverse=True
    )

    sor_fac_inf_dict = dict(sor_fac_inf_dict)

    # Get other faction info
    final_fac_dict = {}
    for doc in json_dict["docs"]:
        for faction in doc["factions"]:
            faction_dict = {}
            fac_name = faction.get("name")
            fac_inf = (
                faction["faction_details"]["faction_presence"]["influence"]
            ) * 100
            fac_inf = f"{fac_inf:.2f}"
            faction_dict.update({"Influence": fac_inf})
            fac_gov = (faction["faction_details"]["government"]).capitalize()
            faction_dict.update({"Government": fac_gov})
            fac_alleg = (faction["faction_details"]["allegiance"]).capitalize()
            faction_dict.update({"Allegiance": fac_alleg})
            fac_happiness = faction["faction_details"]["faction_presence"]["happiness"]
            fac_happiness = h.get_faction_happiness(fac_happiness)
            faction_dict.update({"Happiness": fac_happiness})

            fac_act_states = faction["faction_details"]["faction_presence"][
                "active_states"
            ]
            c_str = ""
            for value in fac_act_states:
                state_fmt = h.get_faction_states(value["state"])
                c_str = c_str + f"{state_fmt}, "
            if c_str == "":
                c_str = "None"
            else:
                c_str = c_str[:-2]
            faction_dict.update({"Active States": c_str})
            final_fac_dict.update({fac_name: faction_dict})

            fac_pen_states = faction["faction_details"]["faction_presence"][
                "pending_states"
            ]
            c_str = ""
            for value in fac_pen_states:
                state_fmt = h.get_faction_states(value["state"])
                c_str = c_str + f"{state_fmt}, "
            if c_str == "":
                c_str = "None"
            else:
                c_str = c_str[:-2]
            faction_dict.update({"Pending States": c_str})
            final_fac_dict.update({fac_name: faction_dict})

            fac_rec_states = faction["faction_details"]["faction_presence"][
                "recovering_states"
            ]
            c_str = ""
            for value in fac_rec_states:
                state_fmt = h.get_faction_states(value["state"])
                c_str = c_str + f"{state_fmt}, "
            if c_str == "":
                c_str = "None"
            else:
                c_str = c_str[:-2]
            faction_dict.update({"Recovering States": c_str})
            final_fac_dict.update({fac_name: faction_dict})

    # Outputs final system data dictionary to file
    fpath = r"data/"
    fname = fpath + sys_name + "_" + tf.time_fname_output()
    with open(fname, "w") as output:
        output.write("[General System Info]\n")
        for key, value in final_dict.items():
            output.write(f"{key}: {value}\n")
        output.write("\n\n")
        output.write("[Faction Influence List]\n")
        for key, value in sor_fac_inf_dict.items():
            output.write(f"{key}: {value:.2f}\n")
        output.write("\n\n")
        output.write("[Detailed Faction Information]\n")
        for key, value in final_fac_dict.items():
            output.write(f"{key}\n")
            for y in value:
                output.write(f"{y}: ")
                val = value[y]
                output.write(f"{val}\n")
            output.write("\n")
        output.write("\n\n")
