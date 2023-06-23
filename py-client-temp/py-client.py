'''
A temporary python client (as no we client yet).

'''
import json

from gserver.http_requests import HttpRequests
from gserver.logger import Alogger
from gserver.db_if.db_models import BoardG4inRow

NUM_COLS = 7
NUM_ROWS = 8

my_logger = Alogger('py_client_test.log')
logger = my_logger.get_logger()

def print_board_matrix(matrix: list):
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            print(matrix[NUM_COLS-1-i][j], end="") #the end= is to avoid CRs
        print("")
    return 0

# Read user selection
read_ok = False
while not read_ok:
    player_id_read = input("enter player id (int): ")
    try:
        player_id = int(player_id_read)
        print(f'your player_id is {player_id}')
        read_ok = True
    except:
        print("err")

# Join the game and register into the server so it can push into the client.

# todo join the game using restApi requests

URL_PREFIX = "http://127.0.0.1:5000/gs/v1"
req = HttpRequests(logger)

logger.debug(f'Check is server is alive:')
url0 = URL_PREFIX + "/status"
code, rjson = req.get(url0)
logger.info(f' json got: {type(rjson)} , {rjson} code: {code}')
if code > 210:
    logger.error("Server access error")
    exit(1)

logger.debug(f'Player 1001 joins:')
url2 = URL_PREFIX + "/game/join/g4inrow"
payload = {"player_id": 1001}
code, rjson = req.post(url2, payload)
logger.info(f' json got: {type(rjson)} , {rjson} code: {code}')
assert rjson == {'room_id': 1, 'room_status': 1}

room_got = rjson

# Print board
print(f'room_got["board"] {type(room_got["board"])} {room_got["board"]}')
board_dict = json.loads(room_got["board"].replace("\'", "\""))
print_board_matrix(board_dict["matrix"])




# print the game board per the received info.
# todo register for webhooks
# todo loop
#   sleep for 30 sec
#   pull the server. If fails exit the game
#   if changed print the board.

#game_end = False
#while not game_end:





if __name__ == "__main__":

    matrix = [["-" for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
    print_board_matrix(matrix)
    pass

