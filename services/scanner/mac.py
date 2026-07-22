import re
import subprocess


def get_mac_address(ip_address):
    """
    Lấy MAC Address từ ARP Cache của Windows.
    Trả về None nếu không tìm thấy.
    """

    try:
        result = subprocess.check_output(
            ["arp", "-a", ip_address],
            text=True,
            encoding="utf-8",
            errors="ignore"
        )

        match = re.search(
            r"([0-9a-fA-F]{2}[-:]){5}[0-9a-fA-F]{2}",
            result
        )

        if match:
            return match.group(0).replace("-", ":")

    except Exception:
        pass

    return None