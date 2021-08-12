##from gserver.board import Board
from gserver.db_if.db_models import *
from gserver.db_if.redis_operations import *

def init_new_board(id):  # !!!!!!! ****** USED
    num_cols = 7
    num_rows = 8
    board = Board(id=id,
                  player="A",       # A or B
                  winner="",        # equals to A, B, Tie, or null ** Note: Common to other games too **
                  matrix=[["-" for x in range(num_cols)] for x in range(num_rows)],  # martix[row][column]
                  next_row=[0 for i in range(num_cols)],  # init the next row available for each col,
                  last_move_col=0,  # init. This is the col of the last move in range 1..number of cols
                  last_move_row=0,  # init. This is the row of the last move in range 1..number of rows
                  last_player=" ")
    return board


def XX_init_new_board():  # !!!!!!! ****** USED
    board = Board()
    board.player = "A"  # init the first player ** Note: Common to other games too **
    board.winner = ""  # equals to A, B, Tie, or null ** Note: Common to other games too **
    board.matrix = [["-" for x in range(self.num_cols)] for x in range(self.num_rows)]  # martix[row][column]
    board.player = "A"  # A or B
    board.next_row = [0 for i in range(self.num_cols)]  # init the next row available for each col

    # the following is used just for user info sent back to the players
    board.last_player = " "  # init.
    board.last_move_row = 0  # init. This is the row of the last move in range 1..number of rows
    board.last_move_col = 0  # init. This is the col of the last move in range 1..number of cols

    return board


class Board4inRow(): ##(Board):
    def __init__(self, room_id = 0, new_game = True):
        ''' Init and write to db. SWhen starts create the board. Afterwards read from the DB'''
        #super(self).__init__()
        self.num_rows = 8
        self.num_cols = 7

        #if new_game:
        #    self.board = self.init_new_board()
        #else:
        #    self.board = self.retrive_board(room_id)

        #board.id = id
        #RoomDBops.insert_board(board)

    def _init_new_board(self):  # !!!!!!! ****** USED
        board = Board()
        board.player = "A"  # init the first player ** Note: Common to other games too **
        board.winner = ""  # equals to A, B, Tie, or null ** Note: Common to other games too **
        board.matrix = [["-" for x in range(self.num_cols)] for x in range(self.num_rows)] # martix[row][column]
        board.player = "A"  # A or B
        board.winner = ""  # equals to A, B, Tie, or null
        board.next_row = [0 for i in range (self.num_cols)]  # init the next row available for each col

        # the following is used just for user info sent back to the players
        board.last_player = " "  # init.
        board.last_move_row = 0  # init. This is the row of the last move in range 1..number of rows
        board.last_move_col = 0  # init. This is the col of the last move in range 1..number of rows

        return board

    def retrive_board(self, id):
        pass


    def print_board(self):
        print("******* printing board ********")
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                print(self.matrix[self.num_rows - 1 - i][j], end="")  # the end= avoids CR
            print("")
        return ()


if __name__ == '__main__':
    # Test by creating a new board

    #create_room


    pass






