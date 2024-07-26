import os
import json

# def load():
#     config_path = os.path.join('config', 'configuration.txt')
#     with open(config_path, 'r') as file:
#         config = file.readlines()
#         return config

def load():
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'configuration.json')
    with open(config_path, 'r') as file:
        config = file.read()
    json_data = json.loads(config)
    return json_data
