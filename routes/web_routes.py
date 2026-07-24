from flask import Blueprint, render_template
from models.computer import Computer

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
from flask import request, redirect
from services.command_service import CommandService


@web_bp.route("/shutdown", methods=["POST"])
def shutdown():

    computer_id = request.form["computer_id"]

    CommandService().create(
        int(computer_id),
        "shutdown"
    )

    return redirect("/")