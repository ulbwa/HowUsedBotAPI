from threading import Thread
from requests import post


class HowUsedBotAPI:
    def __init__(self, bot_id: int, api_token: str, view_token: str) -> None:
        self.api = 'https://qnext.app/bin/webhooks/6438/181/4opQGmB6OlHqqPRM'
        self.view_url = 'https://qnext.app/bin/charts/6438/19/' \
                        '678cf4eb1efb80c5669b1f3b443d38850d4d642f'
        self.bot_id = bot_id
        self.api_token = api_token
        self.view_token = view_token

    def update(self, event_type: str, user_id: int,
               user_register_time: float = None,
               param_1: str = None, param_2: str = None,
               param_3: str = None) -> None:
        data = {"botId": self.bot_id,
                "apiToken": self.api_token,
                "requestType": "event",
                "event": event_type,
                "userId": user_id}

        if user_register_time:
            data['userRegisterTime'] = user_register_time
        if param_1:
            data['param_1'] = param_1
        if param_2:
            data['param_2'] = param_2
        if param_3:
            data['param_3'] = param_3

        Thread(target=post, args=(self.api,),
               kwargs={"data": data}, daemon=True).start()

    def get_stats(self, params: dict) -> str:
        url = self.view_url + '?token=' + self.view_token + '&id=' + str(self.bot_id)
        params = [str(a) + '=' + str(params[a]) for a in params]
        if params:
            url += "&" + "&".join(params)
        return url
