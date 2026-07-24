import requests

from config import SERVER_URL


def command_done(command_id):

    response = requests.post(
        f"{SERVER_URL}/api/command/{command_id}/done",
        timeout=5
    )

    return response.json()