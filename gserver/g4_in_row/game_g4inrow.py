# The 4 in row game logic

from game_base import GameBase
from db_if.db_models import BoardG4inRow
from db_if.redis_operations import RoomRedisOps

class G4inRow(GameBase):
    num_cols = 7
    num_rows = 8

    def init_new_board(self):  #
        board = BoardG4inRow(
                 player="A",  # A or B (room player_1 is always "A" while room player_2 is always "B")
                 winner="",  # equals to A, B, Tie, or null ** Note: Common to other games too **
                 matrix=[["-" for _ in range(self.num_cols)] for _ in range(self.num_rows)],  # martix[row][column]
                 next_row=[0 for i in range(self.num_cols)],  # init the next row available for each col,
                 last_move_col=0,  # init. This is the col of the last move in range 1..number of cols
                 last_move_row=0,  # init. This is the row of the last move in range 1..number of rows
                 last_player=" ")
        return board

    def print_board_matrix(self, matrix: list):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                print(matrix[self.num_rows-1-i][j], end="") #the end= is to avoid CRs
            print("")
        return 0

    def new_move(self, room_ops: RoomRedisOps, got_room, player_symbol, played_column):
        '''Process the new move per the selected column '''
        board = room_ops.get_room_board(got_room)
        print(f' *** HERE **** {type(board)} {board}')
        # Check if your turn
        if board["player"] != player_symbol:
            return -1, "Illegal move: Not your turn"

        # check if a legal move
        if played_column > (self.num_cols - 1) or (played_column < 0):
            # print ("Illegal move: No such column")
            return -1, "Illegal move: No such column"

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
        retcode, winner = self.check_if_wins(board["matrix"], played_row, played_column)
        print("retcode, winner ", retcode, winner)

        if winner:
            board["winner"] = winner
        else:
            # prepare for next move
            board["next_row"][played_column] += 1  # the next row to put in (if col is not full)
            if board["player"] == "A":  # select next player
                board["player"] = "B"
            else:
                board["player"] = "A"

        return 0, board

    def check_if_wins(self, matrix, played_row, played_column):
        '''check if the last move wins the game'''

        # There are 4 options to win. Prepare 4 strings for it.
        # The strings are:
        # teststr[0] for 4 in a row
        # teststr[1] for 4 in a column
        # teststr[2] for 4 i a diagonal that goes down left to right (135 degrees)
        # teststr[3] for 4 i a diagonal that goes down right to left (45 degrees)

        teststr = ["","","",""]
        # The row string
        teststr[0] = "".join(matrix[played_row])  # the row string
        print ("teststr[0]: ",teststr[0])

        # The column string
        teststr[1] = ''
        for i in range(self.num_rows):
            teststr[1] += matrix[i][played_column]
        print(f'teststr[1]: {teststr[1]}')

        # The diagonal top-left to bottom-right
        test2_list = []
        test3_list = []
        # from the played location upwards
        col_to_left = played_column
        col_to_right = played_column
        for row in range(played_row, self.num_rows):
            if col_to_left >= 0:
                test2_list.append(matrix[row][col_to_left])
            col_to_left -= 1
            if col_to_right < self.num_cols:
                test3_list.append(matrix[row][col_to_right])
            col_to_right += 1

        # from the played location downwards
        col_to_right = played_column + 1  # for teststr[2]
        col_to_left = played_column - 1   # for teststr[3]
        for row in reversed(range(played_row)):
            if col_to_right < self.num_cols:
                test2_list.insert(0, matrix[row][col_to_right])
                col_to_right += 1
            if col_to_left >= 0:
                test3_list.insert(0, matrix[row][col_to_left])
                col_to_left -= 1
        teststr[2] = "".join(test2_list)
        teststr[3] = "".join(test3_list)

        print(f'teststr[2]: {teststr[2]}')
        print(f'teststr[3]: {teststr[3]}')

        a_wins = "AAAA"
        b_wins = "BBBB"
        for i in range(4):
            if (teststr[i].find(a_wins) != -1):
                print("A is the winner")
                self.winner = "A"
                return 1, self.winner  # with a winner
            if (teststr[i].find(b_wins) != -1):
                print("B is the winner")
                self.winner = "B"
                return 1, self.winner  # with a winner
        return 0, ""


