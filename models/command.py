from datetime import datetime

from database.db import db


class Command(db.Model):
    __tablename__ = "commands"

    id = db.Column(db.Integer, primary_key=True)

    computer_id = db.Column(
        db.Integer,
        db.ForeignKey("computers.id"),
        nullable=False
    )

    command = db.Column(db.String(100), nullable=False)

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.now
    )

    executed_at = db.Column(
        db.DateTime,
        nullable=True
    )