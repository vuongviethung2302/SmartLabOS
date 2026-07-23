from models.command import Command
from database.db import db


class CommandService:

    def create(self, computer_id, command):

        new_command = Command(
            computer_id=computer_id,
            command=command,
            status="Pending"
        )

        db.session.add(new_command)
        db.session.commit()

        return new_command

    def get_pending_command(self, computer_id):

        return Command.query.filter_by(
            computer_id=computer_id,
            status="Pending"
        ).first()