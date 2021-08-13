from dataclasses import dataclass
import json


@dataclass(eq=True)
class BoardG4inRow:
    id: int
    player: str
    winner: str
    next_row: list
    last_player: str
    last_move_row: int
    last_move_col: int
    matrix: list


@dataclass(eq=True)
class Room:
    '''A game room for for two players.'''
    id: int
    game_type: str  # Currently only G4inRow or none
    room_status: int  # status= 0(Empty), 1(available), 2(full)
    player_1_id: int
    player_2_id: int
    board: dict  # the board.__str__ returns dict


@dataclass(eq=True)   # todo: To delete
class Try:
    '''A game room for for two players.'''
    id: int
    type: str


@dataclass(eq=True)
class RoomsSet:
    id: int


@dataclass(eq=True)
class Player:
    ''' A players '''
    id: int
    name: str
    source: str
    status: int


@dataclass(eq=True)
class PlayersSet:
    '''List of players'''
    id: int


if __name__ == "__main__":
    num_cols = 7
    num_rows = 8
    board0 = BoardG4inRow(id=77,
                          player="A",  # A or B
                          winner="",  # equals to A, B, Tie, or null ** Note: Common to other games too **
                          matrix=[["-" for _ in range(num_cols)] for _ in range(num_rows)],  # martix[row][column]
                          next_row=[0 for i in range(num_cols)],  # init the next row available for each col,
                          last_move_col=0,  # init. This is the col of the last move in range 1..number of cols
                          last_move_row=0,  # init. This is the row of the last move in range 1..number of rows
                          last_player=" ")

    room1 = Room(id=1,
                game_type="G4inRow",
                room_status=0,
                player_1_id=1,
                player_2_id=2,
                board=json.loads(json.dumps(board0.__dict__)))

    print(type(room1))
    print(room1.__str__())

    print("------BOARD0----------")
    print(type(board0.__dict__), type(json.dumps(board0.__dict__)))
    print(json.dumps(board0.__dict__))

    print("-----ROOM1-----------")
    print(type(room1.__dict__), type(json.dumps(room1.__dict__)))

    # In the code the dict will be used
    my_room_dict = room1.__dict__
    print(json.dumps(room1.__dict__))
    my_room_dict["room_status"] = 999
    print(my_room_dict["board"]["id"])
    assert my_room_dict["room_status"] == 999
