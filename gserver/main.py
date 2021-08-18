import json

from game_import import get_game_instance
from gserver.g4_in_row.game_g4inrow import G4inRow

from gserver.db_if.db_main import *
from constants import *


def exe_game_join(request, game_type, dbc, logg):
    logg.debug(f'request & game_type: {request.get_data()} {game_type}')
    request_dict = json.loads(request.get_data().decode("utf-8"))
    player_id = request_dict["player_id"]
    print(f' Player id {player_id}')
    # return {"status": "ok"}
    my_game = G4inRow()
    room_ops = RoomDBops(dbc)
    room_found, room_id, room_status = my_game.find_available_room(G4_IN_ROW, room_ops, player_id)
    print(f'Room_found, room_id, room_status:  {room_found} {room_id} {room_status}')

    msg = {"status": "fail"}
    if room_found:
        if room_status == 1:  # the 1st player
            msg = {"room_status": room_status, "room_id": room_id}
            pass
        elif room_status == 2:  # 2nd player so can start a game
            room_got = room_ops.get_room(room_id)
            print(f'room_got: {type(room_got)} {room_got}')
            msg = room_got
            #msg = {"room_status": room_status, "room_id": room_id}
            #msg = {"room_status": room_status, "room_id": room_id}
            #pass
        else:  # Illegal status
            pass
    else:  # no room available
        msg = {"status": "fail", "message": "No available room found"}
        pass

    return msg

def exe_game_play(request, player_id, dbc, logg):
    logg.debug(f'request & palyer_id: {request.get_data()} {player_id}')
    request_dict = json.loads(request.get_data().decode("utf-8"))
    room_id = request_dict["room_id"]
    played_column = request_dict["played_column"]

    print(f' Room id {room_id}')
    # Verify this player is active on this room
    room_ops = RoomDBops(dbc)
    got_room = room_ops.get_room(room_id)

    if got_room["player_1_id"] == str(player_id):
        player_symbol = 'A'
    elif got_room["player_2_id"] == str(player_id):
        player_symbol = 'B'
    else:
        return {"status": "The player does not exist in the requested room"}

    print(f'got_room {type(got_room)} {got_room}')
    print()
    my_game = get_game_instance(got_room["game_type"].lower())
    print(f' my_game {type(my_game)} {my_game}')

    ret_code, updated_board = my_game.new_move(room_ops, got_room, player_symbol, played_column)
    print(ret_code, updated_board)
    print("The board layout in text: \n")
    my_game.print_board_matrix(updated_board["matrix"])
    # Update DB
    got_room["board"] = str(updated_board)
    print(f'got_room: {type(got_room)} {got_room}')
    room_ops.insert_room_dict(got_room)

    return {"status": "playing"}


def main():
    from set_logger import logger
    logger.error("Stam...")
    # dbc = get_db_client()
    # print(f'DB client: {dbc}')


if __name__ == '__main__':
    main()
