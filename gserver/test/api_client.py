import json
import requests
from http_requests import HttpRequests

from logger import Alogger
my_logger = Alogger('test.log')
logger = my_logger.get_logger()

URL_PREFIX = "http://127.0.0.1:5000/gs/v1"
req = HttpRequests(logger)

logger.debug(f'Check is server is alive:')
url0 = URL_PREFIX + "/status"
code, rjson = req.get(url0)
logger.info(f' json got: {type(rjson)} , {rjson} code: {code}')
if code > 210:
    logger.error("Server access error")
    exit(1)

logger.debug(f'DELETE / Get list:')
url1 = URL_PREFIX + "/game/list/all"
code, rjson = req.delete(url1)
#code, rjson = req.get(url1)
logger.info(f'json got: {type(rjson)} , {rjson} code: {code}')
if code > 210:
    logger.error("Server GET error")
    exit(1)

'''
logger.debug(f' Delete room1 if exists:')

code, rjson = req.delete(url)
logger.info(f' json got: {type(rjson)} , {rjson} code: {code}')
'''

#url = URL_PREFIX + "/room/1" # old
logger.debug(f'Get list after all rooms have been deleted:')
url1 = URL_PREFIX + "/game/list/all"
code, rjson = req.get(url1)
logger.info(f' json got: {type(rjson)} , {rjson} code: {code}')
assert rjson["room ids list"] == []  # Verify all rooms were deleted

logger.debug(f'Player 1001 joins:')
url2 = URL_PREFIX + "/game/join/g4inrow"
payload = {"player_id": 1001}
code, rjson = req.post(url2, payload)
logger.info(f' json got: {type(rjson)} , {rjson} code: {code}')
assert rjson == {'room_id': 1, 'room_status': 1}

logger.debug(f'Player 1002 joins:')
url3 = URL_PREFIX + "/game/join/g4inrow"
payload = {"player_id": 1002}
code, rjson = req.post(url3, payload)
logger.info(f' json got: {type(rjson)} , {rjson} code: {code}')

room_got = rjson
assert room_got["room_status"] == str(2)

# Print board
board_dict = json.loads(room_got["board"].replace("\'", "\""))
from g4_in_row.game_g4inrow import G4inRow
my_game = G4inRow()
my_game.print_board_matrix(board_dict["matrix"])

logger.debug(f'Player 1001 plays:')
payload = {"room_id": 1, "played_column": 1}
urlp1 = URL_PREFIX + '/game/play/1001'
code, rjson = req.post(urlp1, payload)
logger.info(f' json got: {type(rjson)} , {rjson} code: {code}')

# Print board
board_dict = rjson
from g4_in_row.game_g4inrow import G4inRow
my_game = G4inRow()
my_game.print_board_matrix(board_dict["matrix"])
assert board_dict["matrix"][0][1] == 'A' and board_dict["matrix"][1][1] == '-'

# Move not in your turn:
logger.debug(f'Player 1001 plays again not in turn:')
payload = {"room_id": 1, "played_column": 1}
urlp1 = URL_PREFIX + '/game/play/1001'
code, rjson = req.post(urlp1, payload)
logger.info(f' json got: {type(rjson)} , {rjson} code: {code}')

#Illegal move
logger.debug(f'Player 1002 plays illegal move:')
payload = {"room_id": 1, "played_column": 9}
urlp1 = URL_PREFIX + '/game/play/1002'
code, rjson = req.post(urlp1, payload)
logger.info(f' json got: {type(rjson)} , {rjson} code: {code}')


logger.debug(f'Player 1002 plays:')
payload = {"room_id": 1, "played_column": 1}
urlp1 = URL_PREFIX + '/game/play/1002'
code, rjson = req.post(urlp1, payload)
logger.info(f' json got: {type(rjson)} , {rjson} code: {code}')

# Print board
board_dict = rjson
my_game.print_board_matrix(board_dict["matrix"])
assert board_dict["matrix"][0][1] == 'A' and board_dict["matrix"][1][1] == 'B'


logger.info("Test passed")
