from services.scanner.network_scanner import NetworkScanner

scanner = NetworkScanner()

print(scanner.scan_subnet_thread("10.170.45.0/24"))