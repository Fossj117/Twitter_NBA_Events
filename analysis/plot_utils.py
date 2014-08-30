def plot_mentions(mentions_list, tweets, how_often='1t'):
    """
    Helper function for plotting mentions graphs.
    INPUT: 
    - mentions_list: list of strings (mentions)
    - tweets: data frame of tweets with 'text' field
    - how_often: determines size of temporal bins. 
    """
    
    for mention in mentions_list: 
        # Which tweets have this mention?
        mention_bool = tweets.text.str.lower().str.contains(mention.lower()) 

        # Make a variable
        tweets[mention] = 0
        tweets[mention][mention_bool] = 1

    # drop stuff we don't care about
    tweets_plot = tweets.drop(['text','geo', 'source','language', 'screen_name', 'user_location'], axis=1)
    tweets = tweets.drop(mentions_list)
    
    ax = tweets_plot.resample(how_often, how='sum').plot(lw=3, alpha=0.7, colormap='Set1')
    ax.legend(loc='upper center',ncol=4)

    return ax    