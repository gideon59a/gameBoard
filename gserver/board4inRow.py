from gserver.db_if.db_models import Board

def init_new_board(id):  #
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


if __name__ == '__main__':
    # Test by creating a new board

    pass






