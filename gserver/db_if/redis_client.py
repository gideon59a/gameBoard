from redis import StrictRedis  # Use it instead of "import redis" to be able to store dict
from constants import *

host = N_LENOVO_WSL2
port = N_LAP_WSL2_PORT

class RedisClient:

    def __init__(self):
        self.client = StrictRedis(host=host, port=port, db=1, password=None, max_connections=10, decode_responses=True)
        # decode_responses=True is needed so .get will provide "string" rather than b'bytes. Otherwise  .decode() shouold be added to each get.
        self.test_conn()

    def test_conn(self):
        try:
            self.client.set("try", "ok")
            got = self.client.get("try")
            if got == "ok":
                print("connection test ok")
            else:
                print("connection test failed")
        except :  # todo on failure we don't get here, and the following message is not printed
            raise ConnectionError


if __name__ == "__main__":

    r = RedisClient()
    dbc = r.client

    dict_to_store = {"key1": 101, "key2": "val2"}
    result = dbc.hset("test_name", mapping=dict_to_store)  # The whole dict is stored under "test_name"
    got_mydict = dbc.hgetall("test_name")
    print(f'got_mydicty: {type(got_mydict)} {got_mydict}')
    # result_z = rr.hset("mydictz", "zzkey", str(mydictz) )
    assert got_mydict["key1"] == str(101)  # NOTE: Redis returns string instead of a dict
    assert got_mydict["key2"] == "val2"

    ## mset example
    dbc.mset({"Croatia1": "Zagreb1", "Bahamas1": "Nassau1"})
    key0 = dbc.get("Croatia1")
    assert key0 == "Zagreb1"  # Use get to read a specic key.

    key1 = dbc.mget("Croatia1")
    assert key1 == ["Zagreb1"]  # with mset we GOT A LIST

    print("Test passed")

