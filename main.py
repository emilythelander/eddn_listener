import get_last_tick as tick
#import system_list as syslist
import requests
import json
from datetime import datetime

system_list = ["Lanaest","Bildeptu"]


def get_system_data(name):
    url = "https://elitebgs.app/api/ebgs/v5/systems?name=" + name
    response = requests.get(url)

    if response.status_code == 200:
        json_data = json.loads(response.text)

        last_tick = tick.convert_tz(tick.get_last_tick())
        cur_time = datetime.now()
        cur_mon = cur_time.strftime("%m")
        cur_day = cur_time.strftime("%d")
        cur_hour = cur_time.strftime("%H")
        cur_min = cur_time.strftime("%M")
        fpath = r"data/"
        fname = (
            fpath
            + name
            + "_"
            + cur_mon
            + "_"
            + cur_day
            + "_"
            + cur_hour
            + cur_min
            + ".txt"
        )


        try:
            last_update = tick.convert_tz(json_data["docs"][0]["updated_at"])
        except Exception as e:
            with open("error.txt", "a") as errorfile:
                errorfile.write("Data for system " + name + f" either isn't present or has some other issue. {e}")
                errorfile.write(
                "Load failed for "
                + name + " "
                + cur_mon
                + "_"
                + cur_day
                + "_"
                + cur_hour
                + cur_min
            )
            
        
        current = last_update >= last_tick

        sys_dict = {'Last Update':last_update,
                    'Current':current}

        with open(fname, "w") as output:
            for key, value in sys_dict.items():
                output.write('%s:%s\n' % (key, value))

    else:
        with open("error.txt", "a") as errorfile:
            errorfile.write(
                "JSON Load failed for "
                + name
                + cur_mon
                + "_"
                + cur_day
                + "_"
                + cur_hour
                + cur_min
            )


for system in system_list:
    try:
        get_system_data(system)
    except Exception:
        print("Errors occurred, see error log for details.")
        continue

