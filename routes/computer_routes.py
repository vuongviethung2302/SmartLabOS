from flask import Blueprint, render_template
from models.computer import Computer

computer_bp = Blueprint("computer_bp", __name__)

@computer_bp.route("/computers")
def computers():

    computers = Computer.query.all()

    return render_template(
        "computers.html",
        computers=computers
    )