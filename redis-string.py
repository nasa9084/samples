from redis import Redis
redis = Redis()
redis.set('hoge', 'fugafuga')
print(redis.get('hoge'))
#=> b'fugafuga'

redis.set('point', 10)
print(redis.get('point'))
#=> b'10'
redis.incr('point')
print(redis.get('point'))
