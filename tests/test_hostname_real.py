from services.scanner.hostname import get_hostname

ips = [
    "10.170.45.1",
    "10.170.45.129",
    "10.170.45.132"
]

for ip in ips:
    print(ip, "->", get_hostname(ip))