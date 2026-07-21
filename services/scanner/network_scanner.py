from .ping import ping_host
from concurrent.futures import ThreadPoolExecutor, as_completed
import ipaddress


class NetworkScanner:

    def __init__(self):
        pass

    def scan_host(self, ip_address):
        return ping_host(ip_address)

    def scan_subnet(self, subnet):

        online_hosts = []

        network = ipaddress.ip_network(subnet)

        for ip in network.hosts():

            ip = str(ip)

            if self.scan_host(ip):

                online_hosts.append(ip)

        return online_hosts

    def scan_subnet_thread(self, subnet):

        online_hosts = []

        network = ipaddress.ip_network(subnet)

        with ThreadPoolExecutor(max_workers=50) as executor:

            futures = {}

            for ip in network.hosts():

                future = executor.submit(self.scan_host, str(ip))

                futures[future] = str(ip)

            for future in as_completed(futures):

                ip = futures[future]

                if future.result():

                    online_hosts.append(ip)

        return online_hosts