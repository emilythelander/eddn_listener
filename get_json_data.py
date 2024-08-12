import requests
import json
from datetime import datetime
import time_functions as tf


def get_system_data(sys_name):
    url = (
        "https://elitebgs.app/api/ebgs/v5/systems?name="
        + sys_name
        + "&factionDetails=true"
    )
    res = requests.get(url)

    if res.status_code == 200:
        json_dict = res.json()
        return json_dict
    else:
        write_error("get_system_data request failed for non-200 status. Info: ")
        print(
            "Request status code other than 200 received, check error file for more details."
        )


def get_last_tick():
    url = "https://elitebgs.app/api/ebgs/v5/ticks"
    response = requests.get(url)

    if response.status_code == 200:
        json_data = json.loads(response.text)
        last_tick = json_data[0]["time"]
        last_tick = tf.convert_tz(last_tick)
        return last_tick
    else:
        write_error("get_last_tick request failed for non-200 status. Info: ")
        print(
            "Request status code other than 200 received, check error file for more details."
        )


def write_error(message):
    with open("error.txt", "a") as errorfile:
        cur_time = datetime.now()
        errorfile.write(
            message
            + " "
            + cur_time.strftime("%m")
            + "_"
            + cur_time.strftime("%d")
            + "_"
            + cur_time.strftime("%H")
            + cur_time.strftime("%M")
        )
