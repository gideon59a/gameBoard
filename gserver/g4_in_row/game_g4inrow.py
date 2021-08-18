from gserver.game_base import GameBase
from gserver.db_if.db_models import BoardG4inRow
from gserver.db_if.redis_operations import RoomDBops

class G4inRow(GameBase):
    num_cols = 7
    num_rows = 8

    def init_new_board(self, id):  #
        #num_cols = 7
        #num_rows = 8
        board = BoardG4inRow(
                 player="A",  # A or B
                 winner="",  # equals to A, B, Tie, or null ** Note: Common to other games too **
                 matrix=[["-" for x in range(self.num_cols)] for x in range(self.num_rows)],  # martix[row][column]
                 next_row=[0 for i in range(self.num_cols)],  # init the next row available for each col,
                 last_move_col=0,  # init. This is the col of the last move in range 1..number of cols
                 last_move_row=0,  # init. This is the row of the last move in range 1..number of rows
                 last_player=" ")
        return board

    def print_board_matrix(self, matrix: list):
        # print(f'mmmm : {type(matrix)} {matrix}')
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                print(matrix[self.num_rows-1-i][j], end="") #the end= is to avoid CRs
            print("")
        return 0

    def new_move(self, room_ops: RoomDBops, got_room, player_symbol, played_column):
        '''Process the new move per the selected column '''

        # check if a legal move
        if played_column > (self.num_cols - 1) or (played_column < 0):
            # print ("Illegal move: No such column")
            return -1, "Illegal move: No such column"
        board = room_ops.get_room_board(got_room)
        print(f' *** HERE **** {type(board)} {board}')
        #aa = board["next_row"][played_column]
        #print(f' played_column: {aa}')
        if board["next_row"][played_column] == self.num_rows:
            # print ("Illegal move: Column is full")
            return -1, "Illegal move: Column is full"

        #update the board per the player's move
        matrix = board["matrix"]
        print(f'************** {type(matrix)}')
        played_row = board["next_row"][played_column]
        matrix[played_row][played_column] = player_symbol
        #matrix[board["next_row"][played_column]][played_column] = player_symbol

        board["last_player"] = player_symbol
        board["last_move_col"] = played_column
        board["last_move_row"] = played_row

        # validate move (check if game status is changed)
        #val_result = self.validate_move(played_column)
        # print ("val_result",val_result)

        # prepare for next move
        board["next_row"][played_column] += 1  # the next row to put in (if col is not full)
        if board["player"] == "A":  # select next player
            board["player"] = "B"
        else:
            board["player"] = "A"

        return 0, board

