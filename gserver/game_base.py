import abc
from gserver.db_if.redis_operations import RoomDBops
from gserver.constants import *
from gserver.db_if.db_models import Room


class GameBase(abc.ABC):

    @abc.abstractmethod
    def init_new_board(self, id):
        pass

    def find_available_room(self, game_type, room_ops: RoomDBops, player_id):
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
                new_board = self.init_new_board(id=7)
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
                    board=new_board.__str__())
                room_ops.insert_room(new_room)

        return room_found, room_id, room_status

def get_game():
    if DB_TYPE == "redis":
#        # get a redis client
#        redis = RedisClient()
#        return redis.client
        pass