import json

class GetJSON:
    def get_json(self):
        config_file = open('big_bot_config.json', 'r')
        return json.load(config_file)