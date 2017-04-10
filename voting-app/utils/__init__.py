import time
import os
from redis import Redis, ConnectionError


def connect_to_redis(host):
    time.sleep(2)
    print "Connecting to redis"

    while True:
        try:
            password = os.getenv("REDIS_PASSWORD")
            if not password:
                print "Could not find Redis password in $REDIS_PASSWORD"
                exit(1)
            redis = Redis(host=host, db=0, password=password)
            redis.ping()
            print "Connected to redis"
            return redis
        except ConnectionError:
            print "Failed to connect to redis - retrying"
            time.sleep(1)
