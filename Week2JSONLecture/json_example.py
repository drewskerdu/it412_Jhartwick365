import json

with open("text_files/config.json") as json_obj:
    config_data = json.load(json_obj)

config_data["memory"] = "100MB"

with open("text_files/config.json", "w") as json_obj:
    json.dump(config_data, json_obj)
