# When running from power shell, run:
# PS C:\pythonProjects\gameBoard\gserver> C:\Python\Python39\python.exe .\api_gs.py
# A basic check from another PS by: PS C:\Users\agideon> curl.exe http://127.0.0.1:5000/gs/v1/game/list/all
# tailf in power shell: PS C:\pythonProjects\gameBoard\gserver> Get-Content gs.log -Wait

from flask import Flask, jsonify, request
import json
import main

from db_if.db_main import get_db_client
from db_if.redis_operations import RoomRedisOps
from constants import *

from logger import Alogger
my_logger = Alogger('gs.log')
logg = my_logger.get_logger()

app = Flask(__name__)

dbc = get_db_client()

@app.route(BASE_URL + '/v1/status', methods=['GET'])
def server_status():
    msg = {"Status": "Server is alive"}
    return jsonify(json.dumps(msg))

@app.route(BASE_URL + '/v1/game/list/<game_type>', methods=['GET', 'DELETE'])
def game_list(game_type):
    db_ops = RoomRedisOps(dbc, logg)
    logg.debug(f'game_list request.method: {request.method}')

    if request.method == 'GET':
        room_ids = db_ops.get_all_room_ids(game_type)
        msg = {"room ids list": room_ids}
        return jsonify(json.dumps(msg))
    else:  # Delete
        logg.debug(f'**** DELETING ALL {game_type}')
        result = db_ops.delete_all_rooms(game_type)
        return jsonify(json.dumps({"result": result}))


@app.route(BASE_URL + '/v1/room/<room_id>', methods=['DELETE'])
def room(room_id):
    db_ops = RoomRedisOps(dbc, logg)
    logg.debug(f' Deleting room {room_id}')
    if room_id == "all":
        result = db_ops.get_all_room_ids(room_id)
    else:
        result = db_ops.del_room(room_id)
    return jsonify(json.dumps({"result": result}))


@app.route(BASE_URL + '/v1/game/join/<game_type>', methods=['POST'])
def game_join(game_type):
    join_status, code = main.exe_game_join(request, game_type, dbc, logg)
    return jsonify(join_status), code
    #return jsonify(main.exe_game_join(request, game_type, dbc, logg))


@app.route(BASE_URL + '/v1/game/play/<player_id>', methods=['POST'])
def game_play(player_id):
    board_dict, code = main.exe_game_play(request, player_id, dbc, logg)
    return jsonify(board_dict), code


if __name__ == '__main__':
    # With Gunicorn the IP address passes as an env. On development the IP is entered manually.
    api_ip = N_LAP_WSL2
    print(f' Running flask using: {api_ip} {API_PORT}')
    logg.debug(f' Running flask using: {api_ip} {API_PORT}')
    app.run(debug=True)
    #app.run(host=api_vip, port=API_PORT, debug=True, ssl_context=(CERT_FILE, CERT_KEY_FILE))
