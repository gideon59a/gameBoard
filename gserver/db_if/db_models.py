# Ref: https://realpython.com/python-data-classes/

from dataclasses import dataclass, field
import json

# PYTHON TECH NOTES:
# The below dataclass is initialized also with lists which are mutable attributes. Per the error I got as well as per
# https://docs.python.org/3/library/dataclasses.html#mutable-default-values one must use default_factory to init with
# mutable attributes. A useful implementation using lambda was used per
# https://stackoverflow.com/questions/52063759/passing-default-list-argument-to-dataclasses


@dataclass()
class BoardG4inRow:
    # num_rows = 8
    # num_cols = 7
    player: str = "A"  # A or B (room player_1 is always "A" while room player_2 is always "B")
    winner: str = ""  # equals to A, B, Tie, or null ** Note: Common to other games too **
    next_row: list = field(default_factory=lambda: [0 for _ in range(7)])  # Next free row for each of the columns
    last_player: str = ""  # The id of the last one who played
    last_move_row: int = 0  # init. This is the row of the last move in range 1..number of rows
    last_move_col: int = 0  # init. This is the col of the last move in range 1..number of cols
    matrix: list = field(default_factory=lambda: [["-" for _ in range(7)] for _ in range(8)])  # martix[row][column]


@dataclass()
class BoardOther:  # an example to other game type
    some_att: str


@dataclass()
class Room:
    '''A game room for for two players.'''
    id: int = 0
    game_type: str = ""  # Currently only G4inRow or None
    room_status: int = 0  # status= 0(Empty), 1(available), 2(full)
    player_1_id: int = 1
    player_2_id: int = 2
    board: str = ""  # Type must be str to be able to store in redis


#======The below is NOT USED YET =========================================================

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
