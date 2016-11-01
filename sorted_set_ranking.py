#!/usr/bin/env python

from redis import Redis

redis = Redis()

while True:
    print('input member:score> ', end='')
    ipt = input()
    if ipt == 'show':  # command 'show'
        ranking = redis.zrange('ranking', 0, 5, withscores=True)[::-1]
        for i, m in enumerate(ranking):
            values = {
                'rank': i+1,
                'member': m[0].decode(),
                'point': m[1]
            }
            print('{rank}: {member} ({point}pt)'.format(**values))
        continue
    member, score = args.split(':')
    redis.zadd('ranking', member, int(score))
print('good bye')
