import redis
import pickle
import json


def get_connection():
    return redis.Redis()


class RedisClient:

    def __init__(self, connection):
        """Initialize client."""
        self.r = connection

    def set(self, key, value, **kwargs):
        """Store a value in Redis."""
        return self.r.set(key, pickle.dumps(value), **kwargs)

    def set_initial(self, key, value):
        """Store a value in Redis."""
        if not self.get(key):
            self.set(key, value)

    def get(self, key):
        """Retrieve a value from Redis."""
        val = self.r.get(key)
        if val:
            return pickle.loads(val)
        return None

    def dump(self, keys, filename):
        data = {}
        for k in keys:
            data[k] = self.get(k)
        print("storing configuration: %s" % json.dumps(data, indent=2))
        with open(filename, "w") as fp:
            json.dump(data, fp, indent=2)

    def load(self, filename):
        data = {}
        with open(filename) as fp:
            data = json.load(fp)
        print("configuration loaded: %s" % json.dumps(data, indent=2))
        for k in data:
            self.set(k, data[k])



class LittleBerryConfig:
    def  __init__(self, connection):
        self.client = RedisClient(connection)
        self.client.set_initial("cor", (0,0,255))

    @property
    def cor(self):
        return self.client.get("cor")
    @cor.setter
    def cor(self, value):
        self.client.set("cor", value)




class LittleBerryControl:
    def  __init__(self, connection):
        self.client = RedisClient(connection)
        self.client.set_initial("CONTROLloopLeds", 1)


    @property
    def CONTROLloopLeds(self):
        return self.client.get("CONTROLloopLeds")
    @CONTROLloopLeds.setter
    def CONTROLloopLeds(self, value):
        self.client.set("CONTROLloopLeds", value)




