from db_if.redis_operations import *

def redis_operation_test():
    from logger import Alogger
    from db_if.db_models import Room

    my_logger = Alogger('redisop.log')
    logger = my_logger.get_logger()

    from gserver.g4_in_row import game_g4inrow

    my_game = game_g4inrow.G4inRow()
    ############################

    ############################
    ## The below works
    board1 = my_game.init_new_board()
    room11 = Room(
        id=11,
        game_type=G4_IN_ROW,
        room_status=2,
        player_1_id=1,
        player_2_id=2,
        board=str(board1.__dict__))
    # board=str(board1.__dict__))
    # board=board1.__str__())

    logger.debug(f' board1 {type(board1)} {board1}')
    b_dict = str(board1.__dict__)
    logger.debug(f' b_dict {type(b_dict)} {b_dict}')
    logger.debug(f' room11 {type(room11.__dict__)} {room11.__dict__}')

    from gserver.db_if.db_main import get_db_client

    dbc = get_db_client()
    logger.debug(f'DB client: {dbc}')

    room_ops = RoomRedisOps(dbc, logger)
    # res = room_ops.try2(room)  # tested ok

    '''

    room1 = {"id": 100,
            "game_type": G4_IN_ROW,
            "game_status": 0,
            "player_1_id": 1,
            "player_2_id": 22,
            "board": {"matrix": "--"}}

    room2 = {"id": 101,
             "game_type": G4_IN_ROW,
             "game_status": 0,
             "player_1_id": 3,
             "player_2_id": 4,
             "board": {}}

    # Let's start with a simple dict
    result1 = room_ops.del_room(100)  # clean
    #result2 = room_ops.del_room(101)  # clean
    print(f'**** room1 type and value {type(room1)} {room1}')
    result3 = room_ops.insert_room_dict(room1)  # Its id is 100
    print(f'res: {result3}')
    #print(room1.__dict__["id"])
    print(room_ops.get_room(room1["id"]))
    '''

    # now with real room functions
    # result4 = room_ops.del_room(100)  # clean
    result11 = room_ops.del_room(11)  # clean
    result12 = room_ops.insert_room(room11)  # Its id is 100
    logger.debug(f'**** room11 type and value {type(room11)} {room11}')

    got_room_dict = room_ops.get_room(11)
    # print(f'Got room11 {type(got_room_dict)} {got_room_dict}')
    # got_board = got_room_dict["board"]
    # print(f' got_board:  {type(got_board)} {got_board}')
    # got_board_dict = json.loads(got_board.replace("\'", "\""))
    # print(f'Matrix: {got_board_dict["matrix"]}')

    board_dict = room_ops.get_room_board(got_room_dict)
    assert board_dict["player"] == 'A'
    logger.debug(f'Matrix: {board_dict["matrix"]}')

    # Updating the DB
    # ================
    board_dict["player"] = 'B'  # An update example
    logger.debug(f' board_dict: {type(board_dict)} {board_dict}')

    got_room_dict["board"] = str(board_dict)
    logger.debug(f'got_room_dict: {type(got_room_dict)} {got_room_dict}')
    room_ops.insert_room_dict(got_room_dict)

    # update_room = Room(got_room_dict, str(board_dict))
    # print(f'update_room {type(update_room)} {update_room}')

    # TRYIMG THE INIT
    from db_if.db_models import Room

    # board = BoardG4inRow(last_move_row=7)
    board = BoardG4inRow()
    logger.debug(f' ****** board  {type(board)} {board}')
    b_dict = str(board.__dict__)
    logger.debug(f' ****** b_dict {type(b_dict)} {b_dict}')

    new_room55 = Room(
        id=55,
        game_type=G4_IN_ROW,
        room_status=1,
        player_1_id=2001,
        player_2_id=0,
        # board=json.loads(json.dumps(board.__dict__)))
        board=str(board.__dict__))

    logger.debug(f'**** room 55 type and value {type(new_room55)} {new_room55}')

    result55 = room_ops.insert_room(new_room55)  # Its id is 100
    print(f'result55 {result55}')

    # exit(55)
    got_room_dict55 = room_ops.get_room(55)
    board_dict55 = room_ops.get_room_board(got_room_dict55)
    print(board_dict55["player"])
    logger.debug(f'Matrix: {board_dict55["matrix"]}')

    logger.debug("exit ok")
    return 0

if __name__ == "__main__":
    if redis_operation_test() == 0:
        print("redis_operation_test passed")
    else:
        print("redis_operation_test failed")

