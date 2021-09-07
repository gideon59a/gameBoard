from constants import *
from db_if.redis_client import RedisClient
from db_if.redis_operations import RoomRedisOps


def get_db_client() -> RedisClient:
    if DB_TYPE == "redis":
        # get a redis client
        redis = RedisClient()
        return redis.client
    else:
        print("only redis is currently supported")
        exit(1)

# todo The below is used only in tesing in start_room.py so may be deleted. Also, need to add logg to its calling
def get_db_ops(db_client: RedisClient) -> RoomRedisOps :
    if DB_TYPE == "redis":
        # get a redis ops instance
        my_room = RoomRedisOps(db_client)
        return my_room
    else:
        print("only redis is currently supported")
        exit(1)
