import redis
import time
import json

REDIS_POSTS_QUEUE = 'POSTS_QUEUE'
POST_COUNTER = 'POST_COUNTER'

redis_client = redis.Redis(host='redis', port=6379)


def store_count(subreddit):
    """
    Store number of posts for each subreddit.
    """
    return redis_client.zincrby(POST_COUNTER, 1, subreddit)


def consume_posts():
    data = redis_client.rpop(REDIS_POSTS_QUEUE)
    if data:
        subreddit = json.loads(data)['subreddit']
        print(f'Received a post from {subreddit}')
        store_count(subreddit)


if __name__ == '__main__':
    while True:
        consume_posts()