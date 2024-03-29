from db_if.redis_client import *

def redis_client_test():

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
    return 0

if __name__ == "__main__":
    if redis_client_test() == 0:
        print("redis_client_test passed")
    else:
        print("redis_client_test failed")