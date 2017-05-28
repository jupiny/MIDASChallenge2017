import os

import requests


def send_email(sender, receiver, subject, html):
    response = requests.post(
        os.environ.get('MAILGUN_API_MESSAGE_URL'),
        auth=("api", os.environ.get('MAILGUN_API_KEY')),
        data={
            "from": sender,
            "to": [
                receiver,
            ],
            "subject": subject,
            "text": html,
        }
    )
    return response
