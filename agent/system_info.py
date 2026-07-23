import socket
import uuid


def get_computer_name():
    return socket.gethostname()


def get_ip_address():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception:
        return ""


def get_mac_address():
    mac = uuid.getnode()

    return ":".join(
        f"{(mac >> ele) & 0xff:02X}"
        for ele in range(40, -1, -8)
    )