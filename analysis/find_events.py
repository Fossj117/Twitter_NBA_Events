
import pandas as pd
from dateutil.parser import parse

def get_event_summaries(clean_tweets):
	"""
	INPUT: corpus of tweets
	OUTPUT: list of JSON-like objects

	Takes in a corpus of tweets and returns a list 
	of event objects with associated metadata/summary info. 
	"""
	
	# list of events
	events = get_events(clean_tweets)

	# list of summarized events
	event_summaries = [event.get_summary() for event in events]

	return event_summaries

def get_events(clean_tweets):
	"""
	INPUT: pandas DataFrame of tweets w/columns 'text' and 'time'
	OUTPUT: list of events

	Given a corpus of tweets, return a list of 
	event objects that can be fed to summarizer
	"""
	pass


def clean_tweets(raw_tweets):
	"""
	INPUT: raw tweet data DataFrame
	OUTPUT: multi-indexed data frame with 'day', 'hour', 'min' indices
	and 'text' column

	Cleans up tweets and preps for 
	ingestion into the event extraction
	pipeline. 
	"""

	# just keep texxt and time columns
	tweets = raw_tweets[['text', 'time']].copy()
	tweets['ptime'] = pd.to_datetime(pd.Series(tweets['time']))

	tweets['day'] = tweets.ptime.apply(lambda x: x.day)
	tweets['hour'] = tweets.ptime.apply(lambda x: x.hour)
	tweets['minute'] = tweets.ptime.apply(lambda x: x.minute)

	tweets = tweets.set_index(['day', 'hour', 'minute'])
	tweets = tweets[['text']]

	return tweets

def main(): 
	"""
	Main block.
	"""

	# Read in the data
	FNAME = "../data/game2_tweets.csv"
	raw_tweets = pd.read_csv(FNAME)

	# Clean up the data
	clean_tweets = clean_tweets(raw_tweets)

	event_summaries = get_event_summaries(clean_tweets)
	return event_summaries


if __name__ == "__main__":
	main()





