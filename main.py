import get_json_data as gjd
import parse_system_data as psd
# import system_list as syslist

system_list = ["Bildeptu"]

for system in system_list:
    try:
        data = gjd.get_system_data(system)
        psd.parse_system_data(data)
    except Exception as e:
        print(f"Errors occurred, see error log for details. {e}")
        continue
