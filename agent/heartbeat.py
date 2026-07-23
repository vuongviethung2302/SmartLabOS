import requests

from config import SERVER_URL
from system_info import (
    get_computer_name,
    get_ip_address,
    get_mac_address,
)


def create_heartbeat():
    return {
        "computer_name": get_computer_name(),
        "ip_address": get_ip_address(),
        "mac_address": get_mac_address(),
        "agent_version": "1.0.0"
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