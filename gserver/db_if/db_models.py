#Ref: https://realpython.com/python-data-classes/

from dataclasses import dataclass
import json


@dataclass(eq=True)
class BoardG4inRow:
    num_rows = 8
    num_cols = 7
    player: str = "A"  # A or B (room player_1 is always "A" while room player_2 is always "B")
    winner: str = ""  # equals to A, B, Tie, or null ** Note: Common to other games too **
    next_row: list = [0 for i in range(num_cols)],  # The next row available for each of the columns
    last_player: str = "" # The id of the last one who played
    last_move_row: int = 0,  # init. This is the row of the last move in range 1..number of rows
    last_move_col: int = 0,  # init. This is the col of the last move in range 1..number of cols
    matrix: list = [["-" for _ in range(7)] for _ in range(num_rows)],  # martix[row][column]


@dataclass(eq=True)
class BoardOther:  # an example to other game type
    some_att: str


@dataclass(eq=True)
class Room:
    '''A game room for for two players.'''
    id: int = 0
    game_type: str = ""  # Currently only G4inRow or None
    room_status: int = 0  # status= 0(Empty), 1(available), 2(full)
    player_1_id: int = 1
    player_2_id: int = 2
    board: str = ""  # Type must be str to be able to store in redis

    #id: int
    #game_type: str  # Currently only G4inRow or none
    #room_status: int  # status= 0(Empty), 1(available), 2(full)
    #player_1_id: int
    #player_2_id: int
    #board: str  # Type must be str to be able to store

@dataclass(eq=True)
class RoomBase:
    '''A game room for for two players.'''
    id: int = 0
    game_type: str = ""  # Currently only G4inRow or None
    room_status: int = 0  # status= 0(Empty), 1(available), 2(full)
    player_1_id: int = 1
    player_2_id: int = 2
    board: str = ""  ## = field(init=False) # Type must be str to be able to store in redis

'''
@dataclass(eq=True)
class RoomNewBase:   ## WILL BE DELETED
    id: int = 0
    game_type: str = "G4inRow"  # Currently only G4inRow or none
    room_status: int = 0  # status= 0(Empty), 1(available), 2(full)
    player_1_id: int = 1
    player_2_id: int = 2
    board: str = ""  ## = field(init=False) # Type must be str to be able to store

    def __post_init__(self):
        num_cols = 7
        num_rows = 8
        self.board = str(BoardG4inRow(
                 player="A",  # A or B (room player_1 is always "A" while room player_2 is always "B")
                 winner="",  # equals to A, B, Tie, or null ** Note: Common to other games too **
                 matrix=[["-" for _ in range(num_cols)] for _ in range(num_rows)],  # martix[row][column]
                 next_row=[0 for i in range(num_cols)],  # init the next row available for each col,
                 last_move_col=0,  # init. This is the col of the last move in range 1..number of cols
                 last_move_row=0,  # init. This is the row of the last move in range 1..number of rows
                 last_player=" ").__dict__)
'''

@dataclass(eq=True)
class G4inRowRoom(RoomBase):
    def __post_init__(self):
        num_cols = 7
        num_rows = 8
        self.board = str(BoardG4inRow(
                 player="A",  # A or B (room player_1 is always "A" while room player_2 is always "B")
                 winner="",  # equals to A, B, Tie, or null ** Note: Common to other games too **
                 matrix=[["-" for _ in range(num_cols)] for _ in range(num_rows)],  # martix[row][column]
                 next_row=[0 for i in range(num_cols)],  # init the next row available for each col,
                 last_move_col=0,  # init. This is the col of the last move in range 1..number of cols
                 last_move_row=0,  # init. This is the row of the last move in range 1..number of rows
                 last_player=" ").__dict__)


#======NOT USED=========================================================

@dataclass(eq=True)
class xRoomsSet:
    id: int


@dataclass(eq=True)
class xPlayer:
    ''' A players '''
    id: int
    name: str
    source: str
    status: int


@dataclass(eq=True)
class xPlayersSet:
    '''List of players'''
    id: int

print("AAAYYYYYYYYYY")

if __name__ == "__main__":
    from constants import *
    bb = BoardG4inRow()
    print(f'type and value: {type(bb.__dict__)} {bb.__dict__}')
    b1 = json.loads(json.dumps(bb.__dict__))
    b2 = str(bb.__dict__)
    print(f'b1 {type(b1)} {b1}')
    print(f'b2  {type(b2)} {b2}')

    new_room = Room(board=b2)
    room_dict = new_room.__dict__
    print(f'new room dict: {new_room.__dict__}')
    room_id = 100
    room_dict["id"] = room_id
    print(f'modified room_dict {room_dict}')
    exit(888)

if False:
#if __name__ == "__main__":
    from constants import *

    #room_id = 17
    #new_room = RoomNewBase(game_type=G4_IN_ROW, id=17)  # G4inRowRoom()
    #print(type(new_room.__str__), new_room.__str__())  # Returns the whole class, but NOT as a dict
    #room_dict = new_room.__dict__
    #print(type(new_room.__dict__), room_dict) # Returns the dict
    #room_dict["id"] = room_id
    #print(f'modified room_dict {room_dict}')

    new_room = G4inRowRoom(game_type=G4_IN_ROW, id=18)  # G4inRowRoom()
    print(type(new_room.__str__), new_room.__str__())  # Returns the whole class, but NOT as a dict
    room_dict = new_room.__dict__  # dict presentation
    print(type(new_room.__dict__), room_dict)
    room_id = 100
    room_dict["id"] = room_id
    print(f'modified room_dict {room_dict}')

    exit(100)
#=======================================================================
if False:
#if __name__ == "__main__":
    num_cols = 7
    num_rows = 8
    board0 = BoardG4inRow(
                          player="A",  # A or B
                          winner="",  # equals to A, B, Tie, or null ** Note: Common to other games too **
                          matrix=[["-" for _ in range(num_cols)] for _ in range(num_rows)],  # martix[row][column]
                          next_row=[0 for i in range(num_cols)],  # init the next row available for each col,
                          last_move_col=0,  # init. This is the col of the last move in range 1..number of cols
                          last_move_row=0,  # init. This is the row of the last move in range 1..number of rows
                          last_player=" ")

    # The below example is not useful - see room2
    room1 = Room(id=1,
                game_type="G4inRow",
                room_status=0,
                player_1_id=1,
                player_2_id=2,
                board=json.loads(json.dumps(board0.__dict__)))  # no point to use the json here

    ## The below presents the right way to include the borad dataclass within the room dataclass
    room2 = Room(id=1,
                 game_type="G4inRow",
                 room_status=2,
                 player_1_id=21,
                 player_2_id=22,
                 board=board0.__dict__)

    print(type(room1), room1.__str__())  # Returns the whole class, but NOT as a dict

    print("------BOARD0----------")
    print(type(board0.__dict__), board0.__dict__)  # The class DICT !
    print(f'{type(json.dumps(board0.__dict__))}, {json.dumps(board0.__dict__)}')  # The class default __str__
    print(f'matrix: {board0.__dict__["matrix"]}')  # Printing an item from the dict, the matrix.

    print("-----ROOM1-----------")
    print(type(room1.__dict__), room1.__dict__)
    print(type(json.dumps(room1.__dict__)), json.dumps(room1.__dict__))

    # In the code the dict will be used
    my_room_dict = room1.__dict__
    my_room_dict["room_status"] = 999
    #print(f' my_room_dict["board"]["id"]: {my_room_dict["board"]["id"]}')
    print(f'Room1 board matrix: {my_room_dict["board"]["matrix"]}')
    assert my_room_dict["room_status"] == 999

    print("-----ROOM2-----------")
    print(type(room2.__dict__), room2.__dict__)
    print(f'Room2 board matrix: {my_room_dict["board"]["matrix"]}')
    assert room2.__dict__["room_status"] == 2