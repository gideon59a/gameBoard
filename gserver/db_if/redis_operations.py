''' This module implements the access to redis db.
It uimports the abstract methods from dao_base, which in trun imports the db models. '''

from gserver.db_if.redis_client import *
from gserver.db_if.dao_base import *
from gserver.db_if.db_models import *
from constants import *


class RoomDBops(RoomDaoBase):
    def __init__(self):
        self.redis = RedisClient()
        self.r = self.redis.client
        print(f'Ops Redis client: {self.r}')

    def insert_room_dict(self, room: dict, **kwargs) -> int:  # todo - delete
        ''' unused function'''
        print(f'Set id: {room["id"]}')
        self.r.hset("room:"+str(room["id"]), mapping=room)
        return 0

    def insert_room(self, room: Room, **kwargs) -> int:
        room_dict = room.__dict__
        print(f'Set id: {room_dict["id"]}')
        self.r.hset("room:" + str(room_dict["id"]), mapping=room_dict)
        return 0

    def get_room(self, id: int) -> dict:
        print(f"get id: {id}")
        return self.r.hgetall("room:"+str(id))

    def get_root_status(self, id: int) -> int:  # Needed to save getting the whole game
        return self.r.hget("room:" + str(id), "room_status")

    def del_room(self, id: int):
        print(f'deleting room {id}')
        return self.r.delete("room:"+str(id))

    #def get_all_room_names(self) -> list:
    #    return self.r.keys("room:*")

    def get_all_room_ids(self) -> list:
        names_list = self.r.keys("room:*")
        #print(names_list)
        id_list = []
        for name in names_list:
            id = name.split(":")[1]
            id_list.append(int(id))
        return id_list

    def insert_board(self, board: Board ) -> None:
        board_dict = board.__dict__
        print(f'Wr board:  {board_dict["id"]}')
        self.r.hset("room:" + str(board_dict["id"]), mapping=board)

    def get_board(self, id: int) -> dict:
        name = "board:"+str(id)
        print(f'Rd board:  {name}')
        return self.r.hgetall(name)
        
    # XX delete the below
    def try2(self,iroom):
            earth_properties = {
                "diameter_km": "12756",
                "day_length_hrs": "24",
                "mean_temp_c": "15",
                "moon_count": "1"
            }
            # Set the fields of the hash.
            self.r.hset("mytry", mapping=iroom) ##earth_properties)
            print(self.r.hgetall("mytry"))

if __name__ == '__main__':

    from gserver.board4inRow import *
    board1 = init_new_board(id=7)
    room11 = Room(
        id=11,
        game_type="G4inRow",
        room_status=2,
        player_1_id=1,
        player_2_id=2,
        board=board1.__str__())

    room1 = {"id": 100,
            "game_type": "4inRow",
            "game_status": 0,
            "player_1_id": 1,
            "player_2_id": 22,
            "board": ""}

    room2 = {"id": 101,
             "game_type": "4inRow",
             "game_status": 0,
             "player_1_id": 3,
             "player_2_id": 4,
             "board": ""}


    my_room = RoomDBops()
    #res = my_room.try2(room)  # tested ok

    # Let's start with a simple dict
    result1 = my_room.del_room(100)  # clean
    #result2 = my_room.del_room(101)  # clean
    result3 = my_room.insert_room_dict(room1)  # Its id is 100
    print(f'res: {result3}')
    #print(room1.__dict__["id"])
    print(my_room.get_room(room1["id"]))

    # now with real room functions
    #result4 = my_room.del_room(100)  # clean
    result11 = my_room.del_room(11)  # clean
    result12 = my_room.insert_room(room11)  # Its id is 100
    print(my_room.get_room(room11.__dict__["id"]))
    print(f'Room status: {my_room.get_root_status(room11.__dict__["id"])}')


    #res2 = my_room.insert_room(room2)
    #print(my_room.get_room(room2["id"]))


    #list1 = my_room.get_all_room_names()
    #print(list1)
    #for i in list1:
    #    a = i.split(":")
    #    id = a[1]
    #    print(i)
    #    print(a)
    #    print(id)

    #print(my_room.r.hgetall("room:*"))

    print(f'id list: {my_room.get_all_room_ids()}')
