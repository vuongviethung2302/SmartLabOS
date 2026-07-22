from services.scanner.network_scanner import NetworkScanner
import time

scanner = NetworkScanner()

start = time.time()

online = scanner.scan_subnet_thread("10.170.44.0/24")

end = time.time()

print("Online Hosts:", online)
print("Time:", round(end - start, 2), "seconds")
