from database.db import db

class Computer(db.Model):
    __tablename__ = "computers"

    id = db.Column(db.Integer, primary_key=True)
    computer_name = db.Column(db.String(50), unique=True, nullable=False)
    room = db.Column(db.String(10), nullable=False)
    vlan = db.Column(db.Integer, nullable=False)
    ip_address = db.Column(db.String(20), unique=True, nullable=False)
    mac_address = db.Column(db.String(20))
    status = db.Column(db.String(20), default="Offline")
    last_seen = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Computer {self.computer_name}>"