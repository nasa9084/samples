from redis import Redis

redis = Redis()
redis.lpush('piyo', 1, 2, 3)
print(redis.lrange('piyo', 0, -1))
#=> [b'3', b'2', b'1']
print(redis.lpop('piyo'))
#=> b'3'
print(redis.lrange('piyo', 0, -1))
#=> [b'2', b'1']
