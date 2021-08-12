# get the rooms list from the DB, add a new one, store and read
import json
from gserver.db_if.db_models import *
from gserver.board4inRow import *
board1 = init_new_board(id=7)


room1 = Room(
    id=1,
    game_type="G4inRow",
    room_status=2,
    player_1_id=1,
    player_2_id=2,
    board=board1.__str__())

print(board1.__str__())
print(room1.__str__())

