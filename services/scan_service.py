from services.scanner.network_scanner import NetworkScanner
from database.db import db
from models.computer import Computer


class ScanService:

    def __init__(self):

        self.scanner = NetworkScanner()

    def scan_vlan(self, subnet):

        return self.scanner.scan_subnet_thread(subnet)

    def sync_database(self, subnet):

        online_hosts = self.scan_vlan(subnet)

        # Đánh dấu tất cả máy Offline trước
        Computer.query.update(
            {
                "status": "Offline"
            }
        )

        for host in online_hosts:

            computer = Computer.query.filter_by(
                ip_address=host.ip_address
            ).first()

            if computer:

                computer.computer_name = host.computer_name
                computer.mac_address = host.mac_address
                computer.vendor = host.vendor
                computer.status = "Online"

            else:

                computer = Computer(

                    ip_address=host.ip_address,

                    computer_name=host.computer_name,

                    mac_address=host.mac_address,

                    vendor=host.vendor,

                    status="Online"
                )

                db.session.add(computer)

        db.session.commit()

        return len(online_hosts)