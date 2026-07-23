from datetime import datetime

from database.db import db
from models.computer import Computer


class HeartbeatService:

    def process(self, data):

        mac = data.get("mac_address")

        computer = Computer.query.filter_by(
            mac_address=mac
        ).first()

        if computer:

            print(">>> Updating Existing Computer")

            print("Before :", computer.last_seen)

            computer.computer_name = data["computer_name"]
            computer.ip_address = data["ip_address"]
            computer.status = "Online"
            computer.last_seen = datetime.now()

            print("After  :", computer.last_seen)

            db.session.commit()

            db.session.refresh(computer)

            print("DB     :", computer.last_seen)

            print(">>> Update Completed")

        else:

            print(">>> Registering New Computer")

            new_computer = Computer(
                computer_name=data["computer_name"],
                ip_address=data["ip_address"],
                mac_address=data["mac_address"],
                room="UNKNOWN",
                vlan=int(data["ip_address"].split(".")[2]),
                status="Online",
                last_seen=datetime.now(),
            )

            db.session.add(new_computer)
            db.session.commit()

            print(">>> Registration Completed")