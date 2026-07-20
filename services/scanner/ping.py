import subprocess


def ping_host(ip_address):
    """
    Kiểm tra một địa chỉ IP có Online hay không.
    Trả về:
        True  -> Online
        False -> Offline
    """

    command = [
        "ping",
        "-n", "1",
        "-w", "1000",
        ip_address
    ]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0