from flask import Flask
from config import Config
from database.db import db
from routes.computer_routes import computer_bp
from routes.api_routes import api_bp
from routes.web_routes import web_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(computer_bp)
app.register_blueprint(api_bp)
app.register_blueprint(web_bp)

@app.route("/")
def home():
    return "Welcome to SmartLab OS"

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )