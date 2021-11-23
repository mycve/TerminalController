import json
from flask import Blueprint, request, render_template, jsonify, current_app
from config import SPEED

socks5 = Blueprint('socks5', __name__, template_folder=".")


@socks5.route('/socks5/<uid>', methods=['GET', 'POST'])
def __socks5(uid):
    if request.method == "GET":
        return render_template('welcome.html')
    else:
        _code = request.args.get("code")
        print("[*] welcome", _code)
        _data = current_app.cache[uid][0].send_term_command({"v_uid": "0222", "type": "code", "code": _code})
        return jsonify(_data)
