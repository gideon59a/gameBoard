import redis

COMP10 = '10.5.224.10'
COMP10_PORT=3637
N_LAP_WSL2 = "172.18.20.44"
N_LAP_WSL2_PORT = 6379
host = N_LAP_WSL2
port = N_LAP_WSL2_PORT

class RedisClient:

    def __init__(self):
        self.client = redis.Redis(host=host, port=port, db=1, password=None, max_connections=10, decode_responses=True)
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
        except : # todo on failure we don't get here, and the following message is not printed
            raise ConnectionError


if __name__ == "__main__":
    r = RedisClient()
    print(f'r.client: {r.client}')
    r.client.set("c", "xyz")
    print(r.client.get("c"))

    r.client.mset({"Croatia1": "Zagreb1", "Bahamas1": "Nassau1"})
    key1 = r.client.mget("Croatia1")
    result = r.client.mset({"foo": "bar"})
    print(key1)
    print(result)
    print(r.client.get("foo"))
