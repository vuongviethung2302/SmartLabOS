from services.scanner.network_scanner import NetworkScanner

scanner = NetworkScanner()

online = scanner.scan_subnet("127.0.0.0/30")

print(online)