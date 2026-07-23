import requests

from config import SERVER_URL
from heartbeat import create_heartbeat


def get_command():

    data = create_heartbeat()

    response = requests.get(
        f"{SERVER_URL}/api/command",
        params={
            "mac_address": data["mac_address"],
        },
        timeout=5,
    )

    return response.json()