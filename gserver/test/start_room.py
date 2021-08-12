# get the rooms list from the DB, add a new one, store and read
from gserver.pre_game import find_available_room
from gserver.main import get_db_client
dbc = get_db_client()
print(f'DB client: {dbc}')

from gserver.board4inRow import init_new_board
from gserver.db_if.redis_operations import RoomDBops
from gserver.db_if.db_models import Room
board1 = init_new_board(id=7)
my_room = RoomDBops(dbc)

room3 = Room(
    id=3,
    game_type="G4inRow",
    room_status=2,
    player_1_id=1,
    player_2_id=2,
    board=board1.__str__())

room_ids = my_room.get_all_room_ids()
print(room_ids)

room_found, room_id, room_status = find_available_room("G4inRow", my_room ,778)
print(f'Room_found, room_id, room_status:  {room_found} {room_id} {room_status}')



