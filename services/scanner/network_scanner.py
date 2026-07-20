from .ping import ping_host
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