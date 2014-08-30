
import pandas as pd
import numpy as np
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

def get_events(tweets):
	"""
	INPUT: pandas DataFrame of tweets w/columns 'text' and 'time'
	OUTPUT: list of events (dicts w/keys 'time' (tuple), 'tweets' (dataframe))

	Given a corpus of tweets, return a list of 
	events (in some format???)
	"""
	
	PCT_CHNG_THRESH = 0.5

	# volume by minute
	counts = tweets[['text']].groupby(level=[0,1,2]).count()
	event_times = counts[counts.pct_change() > PCT_CHNG_THRESH].dropna().index.tolist()

	events = [{'time':time, 'tweets': tweets.ix[tuple(np.array(time))]} for time in event_times]

	return events

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

	tweets['day'] = tweets.ptime.apply(lambda x: x.day).astype(int)
	tweets['hour'] = tweets.ptime.apply(lambda x: x.hour).astype(int)
	tweets['minute'] = tweets.ptime.apply(lambda x: x.minute).astype(int)

	tweets = tweets.set_index(['day', 'hour', 'minute'])
	tweets = tweets[['text']]

	tweets.sortlevel(inplace=True)

	return tweets
	

if __name__ == "__main__":

	# Read in the data
	FNAME = "./data/game2_tweets.csv"
	raw_tweets = pd.read_csv(FNAME)

	# Clean up the data
	clean_tweets = clean_tweets(raw_tweets)
	#events = get_events(clean_tweets)
	event_summaries = get_event_summaries(clean_tweets)
	#return event_summaries






