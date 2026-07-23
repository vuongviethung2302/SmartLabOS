import socket
import requests

from config import SERVER_URL


def create_heartbeat():
    return {
        "computer_name": socket.gethostname()
    }


def send_heartbeat():
    data = create_heartbeat()

    response = requests.post(
        f"{SERVER_URL}/api/heartbeat",
        json=data,
        timeout=5
    )

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    return response.json()