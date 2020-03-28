from flask import Flask, escape, request, jsonify
import redis
import time

app = Flask(__name__)


cache = redis.Redis(host='redis', port=6379)


def store_count(subreddit):
    """
    Store number of posts for each subreddit.
    """
    return cache.incr("subreddit-{}".format(subreddit))


@app.route('/posts', methods=['POST'])
def consume_posts():
    data = request.json
    subreddit = data['subreddit']
    print(f'Received a post from {subreddit}')
    store_count(subreddit)
    return jsonify({'success': True})