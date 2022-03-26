import json


class Data:
    def get_data(self):
        config_file = open('big_bot_config.json', 'r')
        return json.load(config_file)
    