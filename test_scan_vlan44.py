from services.scanner.network_scanner import NetworkScanner

scanner = NetworkScanner()

hosts = scanner.scan_subnet_thread("10.170.44.0/24")

print(f"Tổng số host: {len(hosts)}")

for host in hosts:
    print(host)