import json
import requests

from bot.settings import FACEBOOK_ACCESS_TOKEN


class Facebook:
    def __init__(self):
        self.sender_id = ''
        self.text = ''

    __post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                         'access_token={}'.format(FACEBOOK_ACCESS_TOKEN)
    __get_profile_info = 'https://graph.facebook.com/v2.6/{sender_id}?' \
                         'fields=first_name,last_name&access_token={TOKEN}'

    # TODO: send
    def send(self, response):
        pass

    def send_message(self):
        response = json.dumps({
            'recipient': {'id': self.sender_id},
            'message': {'text': self.text}
        })

        resp = requests.post(
            self.__post_message_url,
            headers={'Content-Type': 'application/json'},
            data=response
        )

        return resp.content

    # TODO: Send attachment
    def send_attachment(self, type):
        pass

    # TODO: Get profile information like name and email
    def get_profile_info(self):
        resp = requests.get(
            self.__get_profile_info.format(sender_id=self.sender_id, TOKEN=FACEBOOK_ACCESS_TOKEN),
            headers={'Content-type': 'application/json'}
        )

        # name = resp.first_name + resp.last_name

        return resp.content
