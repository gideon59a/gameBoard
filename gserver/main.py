import json
from gserver.g4_in_row.game_g4inrow import G4inRow

from gserver.db_if.db_main import *
from constants import *


def exe_game_join(request, game_type, dbc, logg):
    logg.debug(f'request & game_type: {request.get_data()} {game_type}')
    request_dict = json.loads(request.get_data().decode("utf-8"))
    player_id = request_dict["player_id"]
    print(f' Player id {player_id}')
    #return {"status": "ok"}
    my_game = G4inRow()
    my_room = RoomDBops(dbc)
    room_found, room_id, room_status = my_game.find_available_room(G4_IN_ROW, my_room, player_id)
    print(f'Room_found, room_id, room_status:  {room_found} {room_id} {room_status}')
    return {"status": "ok"}

def main():
    from set_logger import logger
    logger.error("Stam...")
    #dbc = get_db_client()
    #print(f'DB client: {dbc}')


if __name__ == '__main__':
    main()