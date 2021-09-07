# get the rooms list from the DB, add a new one, store and read
print("1111")
from gserver.db_if.db_main import get_db_client
print("1")

from gserver.db_if.db_main import get_db_ops
print("2")

from constants import *
dbc = get_db_client()
my_room = get_db_ops(dbc)
print(f'DB client: {dbc}')


exit(1)


from db_if.db_models import Room
from g4_in_row import game_g4inrow
my_game = game_g4inrow.G4inRow()
board1 = my_game.init_new_board()

room3 = Room(
    id=3,
    game_type="G4inRow",
    room_status=2,
    player_1_id=1,
    player_2_id=2,
    board=board1.__str__())

room_ids = my_room.get_all_room_ids()
print(room_ids)

room_found, room_id, room_status = my_game.find_available_room(G4_IN_ROW, my_room, 778)
print(f'Room_found, room_id, room_status:  {room_found} {room_id} {room_status}')



