from flask import Blueprint, request, jsonify

from models.computer import Computer
from services.heartbeat_service import HeartbeatService
from services.command_service import CommandService

api_bp = Blueprint("api_bp", __name__)


@api_bp.route("/api/heartbeat", methods=["POST"])
def heartbeat():

    data = request.get_json()

    HeartbeatService().process(data)

    return jsonify({
        "success": True
    })


@api_bp.route("/api/command", methods=["GET"])
def get_command():

    mac = request.args.get("mac_address")

    computer = Computer.query.filter_by(
        mac_address=mac
    ).first()

    if not computer:

        return jsonify({
            "success": False,
            "message": "Computer not found"
        }), 404

    command = CommandService().get_pending_command(
        computer.id
    )

    if not command:

        return jsonify({
            "success": True,
            "command": None
        })

    return jsonify({
        "success": True,
        "command": command.command,
        "command_id": command.id
    })


@api_bp.route("/api/command", methods=["POST"])
def create_command():

    data = request.get_json()

    computer_id = data["computer_id"]
    command = data["command"]

    CommandService().create(
        computer_id,
        command
    )

    return jsonify({
        "success": True
    })