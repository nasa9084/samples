from redis import Redis

redis = Redis()
redis.sadd('foo', 1, 3, 5)
print(redis.smembers('foo'))
#=>{b'3', b'5', b'1'}
redis.sadd('foo', 1)
print(redis.smembers('foo'))
#=>{b'3', b'5', b'1'}
