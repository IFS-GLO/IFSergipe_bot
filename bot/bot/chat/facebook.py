import json
import requests

from bot.settings import FACEBOOK_ACCESS_TOKEN


class Facebook:
    def __init__(self):
        self.sender_id = ''
        self.text = ''

    __post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                         'access_token={}'.format(FACEBOOK_ACCESS_TOKEN)

    def send_message(self):
        response_msg = json.dumps({
            'recipient': {'id': self.sender_id},
            'message': {'text': self.text}
        })

        resp = requests.post(
            self.__post_message_url,
            headers={'Content-Type': 'application/json'},
            data=response_msg
        )

        return resp.content
