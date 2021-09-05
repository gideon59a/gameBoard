import json

from game_base import get_game_instance
from db_if.db_main import *


def exe_game_join(request_dict, game_type, dbc, logg):

    player_id = request_dict["player_id"]
    my_game = get_game_instance(game_type)

    room_ops = RoomRedisOps(dbc, logg)
    room_found, room_id, room_status = my_game.find_available_room(game_type, room_ops, player_id)
    logg.debug(f'Room_found, room_id, room_status:  {room_found} {room_id} {room_status}')

    msg, code = {"status": "fail"}, 500  # Init
    if room_found:
        if room_status == 1:  # the 1st player
            msg, code = {"room_status": room_status, "room_id": room_id}, 201
            pass
        elif room_status == 2:  # 2nd player so can start a game
            room_got = room_ops.get_room(room_id)
            logg.debug(f'room_got: {type(room_got)} {room_got}')
            msg, code = room_got, 201
        else:  # Illegal status
            pass
    else:  # no room available
        msg = {"status": "fail", "message": "No available room found"}
        pass

    return msg, code

def exe_game_play(request_dict, player_id, dbc, logg):

    room_id = request_dict["room_id"]
    played_column = request_dict["played_column"]
    logg.debug(f' Room id {room_id}')

    # Verify this player is active on this room
    room_ops = RoomRedisOps(dbc, logg)
    got_room = room_ops.get_room(room_id)

    if got_room["player_1_id"] == str(player_id):
        player_symbol = 'A'
    elif got_room["player_2_id"] == str(player_id):
        player_symbol = 'B'
    else:
        return {"status": "The player does not exist in the requested room"}, 500
    logg.debug(f'for room_id {room_id} got_room {type(got_room)} {got_room}')

    my_game = get_game_instance(got_room["game_type"].lower())
    logg.debug(f' my_game {type(my_game)} {my_game}')

    # play the move
    ret_code, updated_board = my_game.new_move(room_ops, got_room, player_symbol, played_column)
    if ret_code == -1:
        return {"status": "failed", "message": updated_board}, 500

    logg.debug(ret_code, updated_board)
    logg.debug("The board layout in text: \n")
    my_game.print_board_matrix(updated_board["matrix"])

    # Update DB: Update the room per the updated board
    got_room["board"] = str(updated_board)
    logg.debug(f'got_room: {type(got_room)} {got_room}')
    room_ops.insert_room_dict(got_room)

    # todo : delete the room provided the below
    # when I implement the server push to both clients, the room can be deleted here

    return updated_board, 201


def exe_game_get(room_id, player_id, dbc, logg):

    # Verify this player is active on this room
    room_ops = RoomRedisOps(dbc, logg)
    got_room = room_ops.get_room(room_id)

    if got_room["player_1_id"] == str(player_id):
        player_symbol = 'A'
    elif got_room["player_2_id"] == str(player_id):
        player_symbol = 'B'
    else:
        return {"status": "The player does not exist in the requested room"}, 500

    return got_room["board"], 200


def main():
    from logger import Alogger
    my_logger = Alogger('main_test.log')
    logger = my_logger.get_logger()
    logger.error("Stam...")
    # dbc = get_db_client()
    # print(f'DB client: {dbc}')


if __name__ == '__main__':
    main()
