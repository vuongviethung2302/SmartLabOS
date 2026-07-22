from dataclasses import dataclass


@dataclass
class HostInfo:

    ip_address: str

    computer_name: str = ""

    mac_address: str = ""

    vendor: str = ""

    online: bool = False