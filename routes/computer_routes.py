from flask import Blueprint, render_template
from models.computer import Computer
from services.scan_service import ScanService

computer_bp = Blueprint("computer_bp", __name__)

@computer_bp.route("/computers")
def computers():

    computers = Computer.query.all()

    return render_template(
        "computers.html",
        computers=computers
    )

@computer_bp.route("/scan/44")
def scan_vlan44():

    service = ScanService()

    online_hosts = service.sync_online_status("10.170.44.0/24")

    return {
        "message": "Scan completed",
        "online_hosts": online_hosts,
        "count": len(online_hosts)
    }

@computer_bp.route("/scan/45")
def scan_vlan45():

    service = ScanService()

    online_hosts = service.sync_online_status("10.170.45.0/24")

    return {
        "message": "Scan completed",
        "online_hosts": online_hosts,
        "count": len(online_hosts)
    }