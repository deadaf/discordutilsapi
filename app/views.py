from app import app
from flask import jsonify

@app.route("/")
def index():
    return ({"support_guild": "https://discord.gg/aBM5xz6"})

