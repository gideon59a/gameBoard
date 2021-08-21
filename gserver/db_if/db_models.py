#Ref: https://realpython.com/python-data-classes/

from dataclasses import dataclass
import json


@dataclass(eq=True)
class BoardG4inRow:
    player: str  # The player ID
    winner: str
    next_row: list  # The next row available for each of the columns
    last_player: str
    last_move_row: int
    last_move_col: int
    matrix: list
# Note: For now I don't add here the defaults, as it depends on game constants like num_cols, which I was thinking it
# should be part of the game class. todo


@dataclass(eq=True)
class BoardOther:  # an example to other game type
    some_att: str


@dataclass(eq=True)
class Room:
    '''A game room for for two players.'''
    id: int
    game_type: str  # Currently only G4inRow or none
    room_status: int  # status= 0(Empty), 1(available), 2(full)
    player_1_id: int
    player_2_id: int
    board: str  # Type must be str to be able to store


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


if __name__ == "__main__":
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