import socket


def get_hostname(ip_address):
    try:
        return socket.gethostbyaddr(ip_address)[0]
    except Exception:
        return ""
    