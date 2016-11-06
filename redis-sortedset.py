from redis import Redis

redis = Redis()
redis.zadd('bar', 'ham', 20)
redis.zadd('bar', 'egg', 10)
redis.zadd('bar', 'spam', 30)
print(redis.zrange('bar', 0, -1, withscores=True))
#=>[(b'egg', 10.0), (b'ham', 20.0), (b'spam', 30.0)]
