# To run it on the laptop WSL2:
# ip a  ## find the wsl2 ip addr
# sudo vi /etc/redis/redis.conf ## Bind it
# run: # sudo service redis-server restart
# To enter the redis cli run: # sudo redis-cli -h <bind address> (172.17.195.181)
# Update "host" the below code

from redis import StrictRedis  # Use it instead of "import redis" to be able to store dict
from constants import *

#host = N_LENOVO_WSL2
host = "172.18.34.9"
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
