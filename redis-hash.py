from redis import Redis()

redis = Redis()
redis.hset('bar', '0:00', '5')
print(redis.hgetall('bar'))
#=>{b'0:00': b'5'}
add_dict = {
    '1:00': '5',
    '2:00': '6'
}
redis.hmset('bar', add_dict)
print(redis.hkeys('bar'))
#=>[b'0:00', b'1:00', b'2:00]
print(redis.hget('bar', '0:00'))
#=>b'5'
