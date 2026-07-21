from services.scanner.network_scanner import NetworkScanner
import time

scanner = NetworkScanner()

start = time.time()

online = scanner.scan_subnet_thread("127.0.0.0/30")

end = time.time()

print("Online Hosts:", online)
print("Time:", round(end - start, 2), "seconds")
