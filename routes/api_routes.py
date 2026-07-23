from flask import Blueprint, request, jsonify
from models.computer import Computer
from database.db import db

api_bp = Blueprint("api_bp", __name__)


@api_bp.route("/api/heartbeat", methods=["POST"])
def heartbeat():

    data = request.get_json()

    mac = data.get("mac_address")

    computer = Computer.query.filter_by(
        mac_address=mac
    ).first()

    print("=" * 50)
    print("Heartbeat received")
    print(data)

    if computer:

        print(">>> Existing Computer")

    else:

        print(">>> Registering New Computer")

        new_computer = Computer(
            computer_name=data["computer_name"],
            ip_address=data["ip_address"],
            mac_address=data["mac_address"],
            room="UNKNOWN",
            vlan=int(data["ip_address"].split(".")[2]),
            status="Online"
        )

        db.session.add(new_computer)
        db.session.commit()

        print(">>> Registration Completed")

    print("=" * 50)

    return jsonify({
        "success": True,
        "command": "none"
    })