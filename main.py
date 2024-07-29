import get_last_tick as tick
import system_list as syslist
import requests
import json
from datetime import datetime

system_list = ["Grudii"]

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

        last_update = tick.convert_tz(json_data["docs"][0]["updated_at"])
        current = last_update >= last_tick

        with open(fname, "a") as output:
            output.write("Last Update: " + last_update + "\n")
            output.write("Current: " + str(current) + "\n")

    else:
        with open("error.txt", "a") as errorfile:
            errorfile.write(
                "Load failed for "
                + name
                + cur_mon
                + "_"
                + cur_day
                + "_"
                + cur_hour
                + cur_min
            )


for system in system_list:
    get_system_data(system)
