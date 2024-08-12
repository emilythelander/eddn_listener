import get_json_data as gjd
import time_functions as tf

# Takes dictionary as input
def parse_system_data(json_dict):
    
    if type(json_dict) is not dict:
        gjd.write_error("parse_system_data failed due to input object not being type dict. ")
        print("Unable to parse JSON system data, input provided is not a dict object. See error file for more details.")
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
            errorfile.write("Data for system " + sys_name + f" either isn't present or has some other issue. {e}")
        return -1
    
    final_dict = {
        "Name": sys_name
    }

    #Compare update date with last tick to see if the data is current or not
    last_tick = gjd.get_last_tick()
    last_update = json_dict["docs"][0]["updated_at"]
    current = last_update > last_tick
    final_dict.update({"Current": current})

    #Get other basic information we'll always want
    allegiance = json_dict["docs"][0]["allegiance"]
    cmf = json_dict["docs"][0]["controlling_minor_faction_cased"]
        


    
    # Outputs dictionary data to file
    fpath = r"data/"
    fname = (fpath + sys_name 
             + "_"
             + tf.time_fname_output)
    with open(fname, "w") as output:
        for key, value in final_dict.items():
            output.write('%s:%s\n' % (key, value))
    



