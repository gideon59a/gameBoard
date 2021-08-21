import abc
from db_if.redis_operations import RoomRedisOps
from constants import *
from db_if.db_models import Room


class GameBase(abc.ABC):
    ''' The games parent class. The specific game child class will be created per the get_game_instance function.'''

    @abc.abstractmethod
    def init_new_board(self):
        pass

    # The below is common to all games so not abstract
    def find_available_room(self, game_type, room_ops: RoomRedisOps, player_id):
        '''When a new player requests to join/open a game.
        When room_status = 1 the new player can be added to the room'''
        # Start with existing rooms
        room_found = False
        room_id = 0
        room_status = 0
        room_id_list = room_ops.get_all_room_ids()
        print(f' room_id_list {room_id_list}')
        for rid in room_id_list:
            room_status = int(room_ops.get_room_status(rid))
            # print(f'room_status {room_status} {type(room_status)}')
            if room_status == 1:  # There is already a 1st player waiting
                room_id = rid
                room_status = 2
                room_ops.set_att_in_room(room_id, "room_status", room_status)
                room_ops.set_att_in_room(room_id, "player_2_id", player_id)
                room_found = True
                break
        if not room_found:
            if len(room_id_list) < MAX_ROOMS:
                # open a new room
                room_found = True
                new_board = self.init_new_board()
                for i in range(1, 6):
                    if i not in room_id_list:
                        room_id = i
                        break
                room_status = 1
                new_room = Room(
                    id=room_id,
                    game_type=game_type,
                    room_status=room_status,
                    player_1_id=player_id,
                    player_2_id=0,
                    board=str(new_board.__dict__))
                room_ops.insert_room(new_room)

        return room_found, room_id, room_status


def get_game_instance(game_type):
    from g4_in_row.game_g4inrow import G4inRow  # For some reason extracting this import outside the function causes import loop todo
    if game_type == G4_IN_ROW.lower():
        return G4inRow()
    elif game_type == "some other game":
        print("game not supported")
        return 1
