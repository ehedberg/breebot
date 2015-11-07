import praw
import anydbm
import random
import time

db = anydbm.open('seenlist', 'c')

reddit = praw.Reddit(user_agent='Bree Simulator by /u/ehedberg')

reddit.login()


words = ['smoke', 'fire', 'pyro', 'flare', 'flares']

while True:
	print "running"
	subreddit = reddit.get_subreddit('minnesotaunited')

	for comment in subreddit.get_comments():
		interesting = any(string in comment.body.lower() for string in words)
		if interesting and db.has_key(comment.id) == False:
			new_comment = '*N%s%s*' % ('o' * int(random.uniform(8,20)), '!' * int(random.uniform(1,4)))
			comment.reply(new_comment)
			print comment.body
			db[comment.id] = 'T'
	time.sleep(60)
