from flask import Blueprint, render_template, request, redirect

from models.computer import Computer
from services.command_service import CommandService
from services.deployment_service import DeploymentService

web_bp = Blueprint("web_bp", __name__)


@web_bp.route("/")
def dashboard():

    computers = Computer.query.order_by(
        Computer.id
    ).all()

    return render_template(
        "dashboard.html",
        computers=computers
    )


@web_bp.route("/shutdown", methods=["POST"])
def shutdown():

    computer_id = request.form["computer_id"]

    CommandService().create(
        int(computer_id),
        "shutdown"
    )

    return redirect("/")


@web_bp.route("/deploy", methods=["POST"])
def deploy():

    computer_id = request.form["computer_id"]

    computer = Computer.query.get_or_404(
        int(computer_id)
    )

    DeploymentService().deploy(
        computer.ip_address
    )

    return redirect("/")


@web_bp.route("/scan", methods=["POST"])
def scan_network():

    print("=" * 50)
    print("Scan Network Requested")
    print("=" * 50)

    return redirect("/")