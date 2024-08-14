import get_json_data as gjd
import time_functions as tf


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

    """
    Gets the system name and creates the initial dictionary to be used for output later on.
    If the system name doesn't exist in the json file, we know that either it's a dead system
    (i.e. Lanaest) or something is funky with the data and we can't continue.
    """
    try:
        sys_name = json_dict["docs"][0]["name"]
    except Exception as e:
        with open("error.txt", "a") as errorfile:
            errorfile.write(
                "Data for system "
                + sys_name
                + f" either isn't present or has some other issue. {e}"
            )
        return -1

    final_dict = {"Name": sys_name}

    # Compare update date with last tick to see if the data is current or not
    last_update = tf.convert_tz(json_dict["docs"][0]["updated_at"])
    current = tf.is_current(last_update)
    final_dict.update({"Current": current})

    # Get other basic system information we'll always want
    final_dict.update({"Allegiance": json_dict["docs"][0]["allegiance"]})
    final_dict.update({"Government": json_dict["docs"][0]["government"]})
    final_dict.update({"Population": json_dict["docs"][0]["population"]})
    final_dict.update({"Primary Economy": json_dict["docs"][0]["primary_economy"]})
    final_dict.update({"Secondary Economy": json_dict["docs"][0]["secondary_economy"]})
    final_dict.update({"Security": json_dict["docs"][0]["security"]})
    final_dict.update({"System State": json_dict["docs"][0]["state"]})

    #Cycle through system factions, create new dictionary for faction data, sort by inf desc
    uns_fac_dict = {}
    for doc in json_dict["docs"]:
        for faction in doc["factions"]:
            fac_name = faction.get("name")
            fac_inf = faction["faction_details"]["faction_presence"]["influence"]
            uns_fac_dict.update({fac_name: fac_inf})
    
    sor_fac_dict = sorted(uns_fac_dict.items(), key = lambda x:x[1], reverse=True)
    print(sor_fac_dict)


    # Outputs final system data dictionary to file
    fpath = r"data/"
    fname = fpath + sys_name + "_" + tf.time_fname_output()
    with open(fname, "w") as output:
        for key, value in final_dict.items():
            output.write("%s:%s\n" % (key, value))
