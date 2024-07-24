import requests
import json

def get_system_data():
    url = "https://elitebgs.app/api/ebgs/v5/systems?name=Lulus&factionDetails=true"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
system_details = {}
details = get_system_data()
print(json.dumps(details, sort_keys=True, indent=4))