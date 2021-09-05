from constants import *
from db_if.redis_client import RedisClient
print("aaaa")

from db_if.redis_operations import RoomRedisOps
print("aaaabbb")


def get_db_client() -> RedisClient:
    if DB_TYPE == "redis":
        # get a redis client
        redis = RedisClient()
        return redis.client
    else:
        print("only redis is currently supported")
        exit(1)

def get_db_ops(db_client: RedisClient) -> RoomRedisOps :
    if DB_TYPE == "redis":
        # get a redis ops instance
        my_room = RoomRedisOps(db_client)
        return my_room
    else:
        print("only redis is currently supported")
        exit(1)


if __name__ == "__main__":
    print("here db_main")