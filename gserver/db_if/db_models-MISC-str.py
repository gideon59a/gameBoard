from dataclasses import dataclass
import json

@dataclass(eq=True)
class Board:
    id: int
    player: str
    winner: str
    next_row: list
    last_player: str
    last_move_row: int
    last_move_col: int
    matrix: list

    # (Thanks to the __str__, one can get a dict with "print(board.__str__())"
    #def __str__(self):
    #    return {"id": self.id, "player": self.player, "winner": self.winner, "next_row": self.next_row,
    #            "last_player": self.last_player, "last_move_row": self.last_move_row,
    #            "last_move_col": self.last_move_col, "matrix": self.matrix }


@dataclass(eq=True)
class Room:
    '''A game room for for two players.'''
    id: int
    game_type: str  # Currently only G4inRow or none
    room_status: int  # status= 0(Empty), 1(available), 2(full)
    player_1_id: int
    player_2_id: int
    board: dict  # the board.__str__ returns dict

    def __str__(self):
        return {"id": self.id, "game_type": self.game_type, "room_status": self.room_status,
                "player_1_id": self.player_1_id, "player_2_id": self.player_2_id, "board": self.board}



@dataclass(eq=True)
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
    board0 = Board(id=77,
                  player="A",       # A or B
                  winner="",        # equals to A, B, Tie, or null ** Note: Common to other games too **
                  matrix=[["-" for x in range(num_cols)] for x in range(num_rows)],  # martix[row][column]
                  next_row=[0 for i in range(num_cols)],  # init the next row available for each col,
                  last_move_col=0,  # init. This is the col of the last move in range 1..number of cols
                  last_move_row=0,  # init. This is the row of the last move in range 1..number of rows
                  last_player=" ")

    print(f'board.__str__() type = {type(board0.__str__())} ')
    print(board0.__str__())  # A dict returns
    print(json.dumps(board0.__str__()))  # the dict is converted to string. Same result
    ## print(board) will fail as print expects str and got dict

    room1 = Room(id=1,
                game_type="G4inRow",
                room_status=0,
                player_1_id=1,
                player_2_id=2,
                board=board0.__str__())

    print(type(room1))
    print(room1.__str__())

    print("----------------")
    print(type(board0.__dict__), type(json.dumps(board0.__dict__)))
    print(board0.__str__())
    print(json.dumps(board0.__dict__))
    assert  json.dumps(board0.__str__()) == json.dumps(board0.__dict__)  # compare the strings