from services.scanner.network_scanner import NetworkScanner

scanner = NetworkScanner()

online = scanner.scan_subnet("10.170.44.0/24")

print(online)