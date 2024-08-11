import requests
import json
from datetime import datetime
from zoneinfo import ZoneInfo

utc = ZoneInfo("UTC")
local_tz = ZoneInfo("America/Boise")


def get_last_tick():
    url = "https://elitebgs.app/api/ebgs/v5/ticks"
    response = requests.get(url)

    if response.status_code == 200:
        json_data = json.loads(response.text)
        last_tick = json_data[0]["time"]

    return last_tick


def convert_tz(dt):
    td_dt = datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S.%fZ")
    td_local_dt = td_dt.replace(tzinfo=ZoneInfo("UTC")).astimezone(
        ZoneInfo("America/Boise")
    )
    td_local = td_to_str(td_local_dt)

    return td_local

def td_to_str(dt):
    dt_str = datetime.strftime(dt, "%Y-%m-%d %H:%M:%S")
    return dt_str
