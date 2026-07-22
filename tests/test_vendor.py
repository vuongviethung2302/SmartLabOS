from services.scanner.network_scanner import NetworkScanner

scanner = NetworkScanner()

hosts = scanner.scan_subnet_thread("10.170.45.0/24")

for host in hosts:
    print("=" * 50)
    print("IP      :", host.ip_address)
    print("MAC     :", host.mac_address)
    print("Vendor  :", host.vendor)
    print("Hostname:", host.computer_name)
    print("Online  :", host.online)