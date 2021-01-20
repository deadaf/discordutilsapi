from app import app
import secrets
from flask import jsonify

@app.route("/")
def index():
    return ({"support_guild": "https://discord.gg/aBM5xz6"})

@app.route("/password/<nbytes>")
def password(nbytes:int):
    password = secrets.token_urlsafe(int(nbytes))
    return jsonify({"password":password})


@app.errorhandler(404)
def not_found_error(error):
    return ({"error": "404 Page Not Found", "status":"Are you lost baby girl?"}), 404