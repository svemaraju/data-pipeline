from config import reddit
import requests
import json
import time

all_ = reddit.subreddit('all')
publish_url = 'http://consumer:5000/posts'

def publish(data):
	"""
	Post data to a consumer api.
	"""
	response = requests.post(
		publish_url, 
		data=json.dumps(data), 
		headers={'content-type':'application/json'}
	)
	return response


def read():
	"""
	Read reddit's stream of submissions on r/all.
	"""
	count = 0
	for post in all_.stream.submissions():
		# Let's start with publishing 
		# just the subreddit name
		if count > 100: break
		data = {'subreddit': post.subreddit.display_name}
		publish(data)
		print(f'Published {count+1} posts.')
		count += 1
		time.sleep(2) # add a bit of delay


if __name__ == '__main__':
	time.sleep(20)
	print("---- Starting the reddit post stream ----")
	read()