from pprint import pprint

from .messenger import *


class Bot:
    def __init__(self):
        self.THRESHOLD = 0.7

    def first_entity_value(entities, entity):
        if entity not in entities:
            return None

        val = entities[entity][0]['value']

        if not val:
            return None

        return val['value'] if isinstance(val, dict) else val

    """def run_actions(client, message):
        messenger = Facebook()  # Create a Facebook instance
        messenger.sender_id = message['sender']['id']  # save sender id
        messenger.text = message['message']['text']  # save message received from user

        pprint(messenger.get_profile_info())

        resp = client.message(messenger.text)
        # pprint(messenger.sender_id)

        # pprint(resp)

        Facebook.send_message(messenger)
        # send(sender_id, resp['entities']['datetime'][0]['value'])
    """