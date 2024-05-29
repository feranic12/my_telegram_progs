import requests, json, datetime


class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id):
        if (self.get_request(self.get_last_update()) == "Пока!"):
            response = "Пока," + self.get_name(self.get_last_update())
        else:
            response = "Привет," + self.get_name(self.get_last_update())
        params = {'chat_id': chat_id, 'text': response}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        results = self.get_updates()
        if len(results) == 0:
            return None
        else:
            total_updates = len(results) - 1
            return results[total_updates]

    def get_chat_id(self, update):
        chat_id = update['message']['chat']['id']
        return chat_id

    def get_name(self, update):
        name = update['message']['chat']['first_name']
        return name

    def get_request(self, update):
        request = update['message']['text']
        return request


