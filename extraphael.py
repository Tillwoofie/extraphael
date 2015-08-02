import ConfigParser
from twython import Twython

def main(conf):
	for x in conf.keys():
		print " {}: {}".format(x,conf[x])
	
	twit = get_twitter_connection(conf)
	tl = twit.get_home_timeline(count=1, trim_user=True)
	print "timeline tweets"
	for tweet in tl:
		for k in tweet.keys():
			print "{}: {}".format(k, tweet[k])


def get_twitter_connection(conf):
	twitter = Twython(conf['consumer_token'], conf['consumer_secret'],
	                   conf['oauth_token'], conf['oauth_secret'])
	return twitter

def get_config(fname):
	config = ConfigParser.ConfigParser()
	config.read(fname)
	auth = dict(config.items('auth'))
	return auth

if __name__ == '__main__':
	conf = get_config('./main.cfg')
	main(conf)
