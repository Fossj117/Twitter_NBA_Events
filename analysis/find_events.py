

def extract_events(tweets):
	"""
	INPUT: corpus of tweets
	OUTPUT: list of JSON-like objects

	Takes in a corpus of tweets and returns a list 
	of event objects with associated metadata/summary info. 
	"""
	
	# list of events
	events = get_events(tweets)

	# list of summarized events
	event_summaries = [event.get_summary() for event in events]

	return event_summaries

def get_events(tweets):
	"""
	INPUT: corpus of tweets
	OUTPUT: list of events

	Given a corpus of tweets, return a list of 
	event objects that can be fed to summarizer
	"""
	pass




