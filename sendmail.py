import os
import requests


TOKEN = os.environ['MAILGUN_TOKEN']
MAILLIST_NAME = os.environ['MAILLIST_NAME']
EMAIL_FEED_FROM = os.environ['EMAIL_FEED_FROM']
EMAIL_DOMAIN = os.environ['EMAIL_DOMAIN']


def get_list():
    return requests.get(
        f'https://api.eu.mailgun.net/v3/lists/{MAILLIST_NAME}',
        auth=("api", TOKEN),
    )

def send_simple_message():
    lines = []
    with open('email.txt', 'r') as f:
        lines = f.readlines()
    text = ''.join(lines)
    return requests.post(
        f'https://api.eu.mailgun.net/v3/{EMAIL_DOMAIN}/messages',
        auth=("api", TOKEN),
        data={"from": f"DCCN'2019 Conference <{EMAIL_FEED_FROM}>",
              "to": [MAILLIST_NAME],
              "subject": "DCCN'2019 Call for Papers",
              "text": text,
              "template": "dccn2019_2nd_announcement"})


if __name__ == '__main__':
    resp = get_list()
    print(resp.status_code)
    print(resp.content)
