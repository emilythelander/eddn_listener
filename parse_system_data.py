import get_json_data as gjd
import time_functions as tf
import helpers as h
import pandas as pd


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
    allegiance = h.get_allegiance(json_dict["docs"][0]["allegiance"])
    final_dict.update({"Allegiance": allegiance})
    government = h.get_government(json_dict["docs"][0]["government"])
    final_dict.update({"Government": government})
    final_dict.update({"Population": "{:,}".format(json_dict["docs"][0]["population"])})
    prim_eco = h.get_economy(json_dict["docs"][0]["primary_economy"])
    final_dict.update({"Primary Economy": prim_eco})
    sec_eco = h.get_economy(json_dict["docs"][0]["secondary_economy"])
    final_dict.update({"Secondary Economy": sec_eco})
    security = h.get_security(json_dict["docs"][0]["security"])
    final_dict.update({"Security": security})
    state = h.get_state(json_dict["docs"][0]["state"])
    final_dict.update({"System State": state})

    # Get info about conflicts in system
    final_conflict_dict = {}
    count = 1
    for doc in json_dict["docs"]:
        for conflict in doc["conflicts"]:
            conflict_dict = {}
            con_status = conflict.get("status").capitalize()
            con_type = h.get_conflict_type(conflict.get("type"))
            fac1_name = conflict["faction1"]["name"]
            fac1_days_won = conflict["faction1"]["days_won"]
            fac2_name = conflict["faction2"]["name"]
            fac2_days_won = conflict["faction2"]["days_won"]
            conflict_dict.update(
                {
                    "Status": con_status,
                    "Type": con_type,
                    "Faction 1": fac1_name,
                    "Faction 2": fac2_name,
                    "Faction 1 Days Won": fac1_days_won,
                    "Faction 2 Days Won": fac2_days_won,
                }
            )
            final_conflict_dict.update({f"Conflict {count}": conflict_dict})
            count += 1

    # Cycle through system factions, create new dictionary for faction influence data, sort by inf desc
    fac_inf_dict = {}
    for doc in json_dict["docs"]:
        for faction in doc["factions"]:
            fac_name = faction.get("name")
            fac_inf = faction["faction_details"]["faction_presence"]["influence"]
            fac_inf = fac_inf * 100
            fac_inf = round(fac_inf, 2)
            fac_inf_dict.update({fac_name: fac_inf})

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
            fac_alleg = h.get_allegiance(faction["faction_details"]["allegiance"])
            faction_dict.update({"Allegiance": fac_alleg})
            fac_happiness = h.get_faction_happiness(
                faction["faction_details"]["faction_presence"]["happiness"]
            )
            faction_dict.update({"Happiness": fac_happiness})

            fac_act_states = faction["faction_details"]["faction_presence"][
                "active_states"
            ]
            c_str = ""
            for value in fac_act_states:
                state_fmt = h.get_state(value["state"])
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
                state_fmt = h.get_state(value["state"])
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
                state_fmt = h.get_state(value["state"])
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
        gs_df = pd.DataFrame(final_dict.items())
        output.write(
            gs_df.to_string(header=False, index=False, justify="left", col_space=20)
        )
        output.write("\n\n")

        output.write("[System Conflict Info]\n")
        if final_conflict_dict:
            for key, value in final_conflict_dict.items():
                c_status = value["Status"]
                c_type = value["Type"]
                c_f1 = value["Faction 1"]
                c_f2 = value["Faction 2"]
                c_f1dw = value["Faction 1 Days Won"]
                c_f2dw = value["Faction 2 Days Won"]
                output.write(f"{key}:\n{c_type} ({c_status})\n")
                output.write(f"{c_f1} [{c_f1dw}] vs. {c_f2} [{c_f2dw}]\n")
        else:
            output.write("No current conflicts in system\n")
        output.write("\n\n")

        output.write("[Faction Influence List]\n")
        inf_df = pd.DataFrame.from_dict(
            fac_inf_dict, orient="index", columns=["Influence"]
        )
        inf_df = inf_df.sort_values(by="Influence", ascending=False)
        output.write(inf_df.to_string(header=False))
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

        output.write("Detailed Faction Tests\n")
        df_df = pd.DataFrame(final_fac_dict.items())
        output.write(df_df.to_string(header=False, index=False))
