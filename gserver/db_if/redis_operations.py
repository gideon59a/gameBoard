''' This module implements the access to redis db.
It uimports the abstract methods from dao_base, which in trun imports the db models. '''

from gserver.db_if.dao_base import *
from gserver.db_if.db_models import *
from gserver.constants import *

class RoomDBops(RoomDaoBase):
    def __init__(self, db_client):
        super().__init__(db_client)

    def insert_room_dict(self, room: dict, **kwargs) -> int:  # todo - delete
        ''' unused function'''
        print(f'Set id: {room["id"]}')
        print(f' ***insert*** room type and value {type(room)} {room}')
        self.dbc.hset("room:"+str(room["id"]), mapping=room)
        return 0

    def insert_room(self, room: Room, **kwargs) -> int:
        room_dict = room.__dict__
        print(f' INSERT ROOM {type(room_dict)} {room_dict}')
        print(f'Set id: {room_dict["id"]}')
        #dict_to_store = {"key1": 101, "key2": str({"kk2": 22})}
        #self.dbc.hset("tryzz", mapping=dict_to_store)
        #xx self.dbc.hmset("room:" + str(room_dict["id"]), room_dict)
        self.dbc.hset("room:" + str(room_dict["id"]), mapping=room_dict)
        return 0

    def get_room(self, room_id: int) -> dict:
        print(f"get id: {room_id}")
        return self.dbc.hgetall("room:"+str(room_id))

    def get_room_status(self, room_id: int) -> int:  # Needed to save getting the whole game
        print(f' DEBUG *** HERE AT redis_operations ***')
        #? aa = self.get_room(room_id)
        #? print(type(aa))
        #? print(f' DEBUG Print room\n {aa}')
        return self.dbc.hget("room:" + str(room_id), "room_status")

    def get_room_board(self, room_dict: dict) -> dict:
        got_board = room_dict["board"]
        print(f' got_board:  {type(got_board)} {got_board}')
        got_board_dict = json.loads(got_board.replace("\'", "\""))
        return got_board_dict

    def del_room(self, room_id: int):
        print(f'deleting room {room_id}')
        return self.dbc.delete("room:"+str(room_id))

    def get_all_room_ids(self, game_type="") -> list:
        ''' print all room ids (not the full names) for the selected game_type. Default=all types'''
        print(f'getting ids for game_type {game_type}')
        names_list = self.dbc.keys("room:*")
        id_list = []
        for name in names_list:
            #print(f' the name and its content: {name} {self.dbc.hgetall(name)}')
            #print(f'Got game_type {self.dbc.hget(name, "game_type")} for name {name}')
            #got_game_type = self.dbc.hget(name, "game_type")
            #print(f'type: {type(got_game_type)}, lower: {got_game_type.lower()}  ')
            if not game_type or game_type == 'all' or self.dbc.hget(name, "game_type").lower() == game_type:
                rid = name.split(":")[1]
                id_list.append(int(rid))
        return id_list

    def set_att_in_room(self, rid: int, att, value):
        self.dbc.hset("room:" + str(rid), att, value)

    def delete_all_rooms(self, game_type=""):
        room_ids_list = self.get_all_room_ids()   ##self.dbc.keys("room:*")
        for room_id in room_ids_list:
            if not game_type or self.dbc.hget("room:" + str(id), "game_type") == game_type:
                print("deleting room room_id")
                self.del_room(room_id)


    ## The below is currently not used

    def xinsert_board(self, board: BoardG4inRow) -> None:
        board_dict = board.__dict__
        print(f'Wr board:  {board_dict["id"]}')
        self.dbc.hset("room:" + str(board_dict["id"]), mapping=board)

    def xget_board(self, room_id: int) -> dict:
        board_got = self.get_room(room_id)["board"]
        #print(f'Rd board:  {name}')  zzzzz
        #return self.dbc.hgetall(name)
        return {"a": -999}
        
    # XX delete the below
    def try2(self,iroom):
            earth_properties = {
                "diameter_km": "12756",
                "day_length_hrs": "24",
                "mean_temp_c": "15",
                "moon_count": "1"
            }
            # Set the fields of the hash.
            self.dbc.hset("mytry", mapping=iroom) ##earth_properties)
            print(self.dbc.hgetall("mytry"))

if __name__ == '__main__':
    from gserver.db_if.db_models import Room
    from gserver.g4_in_row import game_g4inrow
    my_game = game_g4inrow.G4inRow()
    board1 = my_game.init_new_board(id=7)


    ###from gserver.board4inRow import *
    ###board1 = init_new_board(id=7)
    room11 = Room(
        id=11,
        game_type=G4_IN_ROW,
        room_status=2,
        player_1_id=1,
        player_2_id=2,
        board=str(board1.__dict__))
        #board=str(board1.__dict__))
        #board=board1.__str__())

    print(f' room11 {type(room11.__dict__)} {room11.__dict__}')

    from gserver.db_if.db_main import get_db_client
    dbc = get_db_client()
    print(f'DB client: {dbc}')

    room_ops = RoomDBops(dbc)
    #res = room_ops.try2(room)  # tested ok

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
    print(f'**** room11 type and value {type(room11)} {room11}')

    got_room_dict = room_ops.get_room(11)
    #print(f'Got room11 {type(got_room_dict)} {got_room_dict}')
    #got_board = got_room_dict["board"]
    #print(f' got_board:  {type(got_board)} {got_board}')
    #got_board_dict = json.loads(got_board.replace("\'", "\""))
    #print(f'Matrix: {got_board_dict["matrix"]}')

    board_dict = room_ops.get_room_board(got_room_dict)
    assert board_dict["player"] == 'A'
    print(f'Matrix: {board_dict["matrix"]}')

    # Updating the DB
    #================
    board_dict["player"] = 'B'  # An update example
    print(f' board_dict: {type(board_dict)} {board_dict}')

    got_room_dict["board"] = str(board_dict)
    print(f'got_room_dict: {type(got_room_dict)} {got_room_dict}')
    room_ops.insert_room_dict(got_room_dict)

    #update_room = Room(got_room_dict, str(board_dict))
    #print(f'update_room {type(update_room)} {update_room}')




    print("exit")


