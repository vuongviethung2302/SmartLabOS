from database.db import db


class Device(db.Model):
    __tablename__ = "devices"

    id = db.Column(db.Integer, primary_key=True)

    device_name = db.Column(db.String(100), nullable=False)

    device_type = db.Column(db.String(30), default="Unknown")

    room = db.Column(db.String(20), default="Unknown")

    vlan = db.Column(db.Integer)

    ip_address = db.Column(db.String(20), unique=True, nullable=False)

    mac_address = db.Column(db.String(20), unique=True)

    manufacturer = db.Column(db.String(50))

    model = db.Column(db.String(50))

    os = db.Column(db.String(50))

    cpu = db.Column(db.String(100))

    ram_gb = db.Column(db.Integer)

    status = db.Column(db.String(20), default="Offline")

    def __repr__(self):
        return f"<Device {self.device_name}>"