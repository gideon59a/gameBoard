from constants import *
from gserver.db_if.redis_client import RedisClient
from gserver.db_if.redis_operations import RoomDBops


def get_db_client() -> RedisClient:
    if DB_TYPE == "redis":
        # get a redis client
        redis = RedisClient()
        return redis.client
    else:
        print("only redis is currently supported")
        exit(1)

def get_db_ops(db_client: RedisClient) -> RoomDBops :
    if DB_TYPE == "redis":
        # get a redis ops instance
        my_room = RoomDBops(db_client)
        return my_room
    else:
        print("only redis is currently supported")
        exit(1)


