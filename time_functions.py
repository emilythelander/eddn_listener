from datetime import datetime
from zoneinfo import ZoneInfo

utc = ZoneInfo("UTC")
local_tz = ZoneInfo("America/Boise")

# takes input type string, returns type datetime
def convert_tz(dt):
    td_dt = datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S.%fZ")
    td_local = td_dt.replace(tzinfo=ZoneInfo("UTC")).astimezone(
        ZoneInfo("America/Boise")
    )
    return td_local

# takes input type datetime, returns type string
def td_to_str(dt):
    dt_str = datetime.strftime(dt, "%Y-%m-%d %H:%M:%S")
    return dt_str

def time_fname_output():
    cur_time = datetime.now()
    cur_mon = cur_time.strftime("%m")
    cur_day = cur_time.strftime("%d")
    cur_hour = cur_time.strftime("%H")
    cur_min = cur_time.strftime("%M")
    fname = (
        cur_mon
        + "_"
        + cur_day
        + "_"
        + cur_hour
        + cur_min
        + ".txt"
    )
    return fname

