# Một phần nhỏ của OUI Database.
# Sau này chúng ta sẽ mở rộng lên hàng nghìn hãng.

VENDORS = {
    "00:15:5D": "Microsoft Hyper-V",
    "00:50:56": "VMware",
    "08:00:27": "Oracle VirtualBox",
    "3C:52:82": "Dell",
    "FC:34:97": "HP",
    "00:1B:54": "Cisco",
}


def get_vendor(mac_address):

    if not mac_address:
        return "Unknown"

    prefix = mac_address.upper()[0:8]

    return VENDORS.get(prefix, "Unknown")