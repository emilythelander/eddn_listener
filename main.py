import get_json_data as gjd
import parse_system_data as psd
#import system_list as syslist

system_list = ["Lanaest","Bildeptu"]

for system in system_list:
    try:
        data = gjd.get_system_data()
        psd.parse_system_data(data)
    except Exception:
        print("Errors occurred, see error log for details.")
        continue

