from constants import *
from gserver.db_if.redis_client import RedisClient


def get_db_client():
    if DB_TYPE == "redis":
        # get a redis client
        redis = RedisClient()
        return redis.client

def get_db_ops():
    if DB_TYPE == "redis":
        # get a redis ops instance

