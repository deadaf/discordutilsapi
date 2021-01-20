from app import app
import config
import secrets
from flask import jsonify,request

@app.route("/")
def index():
    return jsonify({"support_guild": "https://discord.gg/aBM5xz6",
    "endpoints":[
        "GET /password?length=int"
    ]})

@app.route("/password")
def password():
    nbytes = request.args.get('length')
    if not nbytes:
        return jsonify({"error":"Password length was not specified"})

    if not isinstance(nbytes, int):
        return jsonify({"error":"length is always an integer dummy!"})

    password = secrets.token_urlsafe(int(nbytes))
    return jsonify({"password":password})


@app.errorhandler(404)
def not_found_error(error):
    return ({"code":404,"error": "Page Not Found", "status":"Are you lost baby girl?"}), 404