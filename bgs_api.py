import requests
import json
from datetime import datetime
from zoneinfo import ZoneInfo

system_list = ["Anhualm","Ankayo","Bildeptu","Bipek","Coanoa","Djamburii","Grudii","HIP 117187","HIP 118169","Kwelenii","Lulus","Maon",
               "Maric","Mati Chuqui","Pictavul","Qa'wakwanga","Quile","Rathamas","Ugrici","Witsanukam","Yankas","Zenmait","Zi Guo Wu"]


utc = ZoneInfo('UTC')
local_tz = ZoneInfo("America/Boise")


def get_system_data(name):
    url = "https://elitebgs.app/api/ebgs/v5/systems?name=" + name
    response = requests.get(url)

    if response.status_code == 200:

        cur_time = datetime.now()
        cur_mon = cur_time.strftime("%m")
        cur_day = cur_time.strftime("%d")
        cur_hour = cur_time.strftime("%H")
        cur_min = cur_time.strftime("%M")
        fpath = r"data/"
        fname = fpath + name + '_' + cur_mon + '_' + cur_day + '_' + cur_hour + cur_min + '.json'

        with open(fname, 'w') as f:
            json.dump(response.json(), f, sort_keys=True, indent=4, ensure_ascii = False)
        
        with open(fname, 'r+') as f:
            data = json.load(f)
            time_string = data['docs'][0]['updated_at']
            time = datetime.strptime(time_string, '%Y-%m-%dT%H:%M:%S.%fZ')
            time_local = time.replace(tzinfo=ZoneInfo('UTC')).astimezone(ZoneInfo('America/Boise'))
            time_local_string = time_local.strftime("%Y-%m-%d %H:%M:%S")
            data['docs'][0]['updated_at'] = time_local_string
            f.seek(0)
            json.dump(data, f, sort_keys=True, indent=4, ensure_ascii = False, default=str)
            f.truncate()
        
        return
    else:
        with open('error.txt', 'w') as errorfile:
            errorfile.write("Load failed for " + name)
        return
        
    
for sys_name in system_list:
    details = get_system_data(sys_name)

