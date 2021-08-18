from flask import Flask, jsonify, request
import json
import main

#from logging import DEBUG, INFO, ERROR
#from set_logger import logger
from gserver.db_if.db_main import get_db_client
from gserver.db_if.redis_operations import RoomDBops
import set_logger
from constants import *

set_logger.logger.info("here")
logg = set_logger.logger
app = Flask(__name__)

dbc = get_db_client()


@app.route(BASE_URL + '/v1/game/list/<game_type>', methods=['GET'])
def game_list(game_type):
    db_ops = RoomDBops(dbc)
    room_ids = db_ops.get_all_room_ids(game_type)
    return jsonify(json.dumps(room_ids))


@app.route(BASE_URL + '/v1/game/join/<game_type>', methods=['POST'])
def game_join(game_type):
    #print(request.json)
    #print(f' TYPE & GET_DATA         : {type(request.get_data())} {request.get_data()}')
    #print(f' TYPE & GET_DATA decoded : {type(request.get_data())} {request.get_data().decode("utf-8")}')
    #print(f' JSON::: {request.get_json}')
    #print(request.method)
    #print(request.__dict__)
    return jsonify(main.exe_game_join(request, game_type, dbc, logg))


@app.route(BASE_URL + '/v1/game/play/<player_id>', methods=['POST'])
def game_play(player_id):
    return jsonify(main.exe_game_play(request, player_id, dbc, logg))


if __name__ == '__main__':
    # With Gunicorn the IP address passes as an env. On development the IP is entered manually.
    api_ip = N_LAP_WSL2
    print(f' Running flask using: {api_ip} {API_PORT}')
    logg.debug(f' Running flask using: {api_ip} {API_PORT}')
    app.run(debug=True)
    #app.run(host=api_vip, port=API_PORT, debug=True, ssl_context=(CERT_FILE, CERT_KEY_FILE))
