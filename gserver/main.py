from gserver.db_if.redis_client import *
from constants import *

def join_game():

    #find_new_room

    pass

#def get_db_client():
#    if DB_TYPE == "redis":
#        # get a redis client
#        redis = RedisClient()
#        return redis.client


def main():
    dbc = get_db_client()
    print(f'DB client: {dbc}')


if __name__ == '__main__':
    main()