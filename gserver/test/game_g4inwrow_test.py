import copy
from game_g4inrow import G4inRow

from logger import Alogger
my_logger = Alogger('test.log')
logger = my_logger.get_logger()


def game_g4inrow_test(logger):
    game = G4inRow()
    matrix = [["-" for _ in range(game.num_cols)] for _ in range(game.num_rows)]

    matrix0 = copy.deepcopy(matrix)
    for i in range(4):
        matrix0[7][i + 1] = 'A'
    print("\nmatrix0:")
    game.print_board_matrix(matrix0)
    retcode, winner = game.check_if_wins(matrix0, 7, 3)
    print(f'win1: {winner}')
    logger.debug(f'matrix0 winner is {winner}')
    if winner != 'A':
        return 1, "failed on matrix0"
    #assert winner == 'A'

    matrix1 = copy.deepcopy(matrix)
    for i in range(4):
        matrix1[i][5] = 'A'
    print("\nmatrix1:")
    game.print_board_matrix(matrix1)
    retcode, winner = game.check_if_wins(matrix1, 3, 5)
    print(f'win1: {winner}')
    logger.debug(f'matrix1 winner is {winner}')
    if winner != 'A':
        return 1, "failed on matrix1"
    #assert winner == 'A'

    matrix2 = copy.deepcopy(matrix)
    # game.print_board_matrix(matrix2)
    matrix2[3][5] = 'B'
    matrix2[4][4] = 'B'
    matrix2[5][3] = 'B'
    matrix2[6][2] = 'B'
    print("\nmatrix2:")
    game.print_board_matrix(matrix2)
    retcode, winner = game.check_if_wins(matrix2, 3, 5)
    print(f'win2: {winner}')
    logger.debug(f'matrix2 winner is {winner}')
    if winner != 'B':
        return 1, "failed on matrix2"
    #assert winner == 'B'

    matrix3 = copy.deepcopy(matrix)
    # game.print_board_matrix(matrix2)
    matrix3[0][6] = 'B'
    matrix3[1][5] = 'B'
    matrix3[2][4] = 'B'
    matrix3[3][3] = 'B'
    print("\nmatrix3:")
    game.print_board_matrix(matrix3)
    retcode31, winner31 = game.check_if_wins(matrix3, 1, 5)
    retcode32, winner32 = game.check_if_wins(matrix3, 3, 3)

    print(f'win3: {winner31} {winner32}')
    logger.debug(f'matrix3 winner is {winner31} = {winner32}')

    if winner31 != 'B' or winner32 != 'B':
        return 1, "failed on matrix3"
    #assert winner31 == 'B' and winner32 == 'B'

    matrix4 = copy.deepcopy(matrix)
    # game.print_board_matrix(matrix2)
    matrix4[2][2] = 'A'
    matrix4[3][3] = 'A'
    matrix4[4][4] = 'A'
    matrix4[5][5] = 'A'
    print("\nmatrix4:")
    game.print_board_matrix(matrix4)
    retcode41, winner41 = game.check_if_wins(matrix4, 5, 5)
    retcode42, winner42 = game.check_if_wins(matrix4, 3, 3)

    print(f'win4: {winner41} {winner42}')
    logger.debug(f'matrix4 winner is {winner41} = {winner42}')
    if winner41 != 'A' or winner42 != 'A':
        return 1, "failed on matrix4"
    #assert winner41 == 'A' and winner42 == 'A'

    return 0, "Test passed"

if __name__ == '__main__':
    logger.debug("Locally testing")
    test_result = game_g4inrow_test(logger)
    print(test_result)
