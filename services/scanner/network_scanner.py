from concurrent.futures import ThreadPoolExecutor, as_completed
import ipaddress

from .ping import ping_host
from .hostname import get_hostname
from .mac import get_mac_address
from .host_info import HostInfo


class NetworkScanner:

    def __init__(self):
        pass

    def scan_host(self, ip_address):
        return ping_host(ip_address)

    def get_host_info(self, ip_address):

        if not ping_host(ip_address):
            return None

        return HostInfo(
            ip_address=ip_address,
            computer_name=get_hostname(ip_address),
            mac_address=get_mac_address(ip_address),
            online=True
        )

    def scan_subnet(self, subnet):

        online_hosts = []

        network = ipaddress.ip_network(subnet)

        for ip in network.hosts():

            host = self.get_host_info(str(ip))

            if host:
                online_hosts.append(host)

        return online_hosts

    def scan_subnet_thread(self, subnet):

        online_hosts = []

        network = ipaddress.ip_network(subnet)

        with ThreadPoolExecutor(max_workers=50) as executor:

            futures = {}

            for ip in network.hosts():

                future = executor.submit(self.get_host_info, str(ip))

                futures[future] = str(ip)

            for future in as_completed(futures):

                host = future.result()

                if host:

                    online_hosts.append(host)

        return online_hosts