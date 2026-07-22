from services.scanner.network_scanner import NetworkScanner
from database.db import db
from models.computer import Computer


class ScanService:

    def __init__(self):
        self.scanner = NetworkScanner()

    def scan_vlan(self, subnet):

        online_hosts = self.scanner.scan_subnet_thread(subnet)

        return online_hosts

    def sync_online_status(self, subnet):

        online_hosts = self.scan_vlan(subnet)

        computers = Computer.query.all()

        for computer in computers:

            if str(computer.ip_address) in online_hosts:
                computer.status = "Online"
            else:
                computer.status = "Offline"

        db.session.commit()

        return online_hosts