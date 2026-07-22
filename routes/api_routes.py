from flask import Blueprint, request, jsonify

api_bp = Blueprint("api_bp", __name__)


@api_bp.route("/api/heartbeat", methods=["POST"])
def heartbeat():

    data = request.get_json()

    print("=" * 50)
    print("Heartbeat received")
    print(data)
    print("=" * 50)

    return jsonify({
        "success": True,
        "command": "none"
    })
