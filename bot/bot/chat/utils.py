import json

from pprint import pprint

import requests

from bot.settings import FACEBOOK_ACCESS_TOKEN


def first_entity_value(entities, entity):
    if entity not in entities:
        return None

    val = entities[entity][0]['value']

    if not val:
        return None

    return val['value'] if isinstance(val, dict) else val


def run_actions(client, message):
    sender_id = message['sender']['id']
    text = message['message']['text']

    resp = client.message(text)

    pprint(resp)
    # pprint(first_entity_value(resp['entities'], 'location'))

    # send(sender_id, resp['entities']['datetime'][0]['value'])


def send(sender_id, text):
    return fb_message(sender_id, text)


def fb_message(sender_id, text):
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(FACEBOOK_ACCESS_TOKEN)

    response_msg = json.dumps({
        'recipient': {'id': sender_id},
        'message': {'text': text}
    })

    resp = requests.post(
        post_message_url,
        headers={'Content-Type': 'application/json'},
        data=response_msg
    )

    return resp.content

