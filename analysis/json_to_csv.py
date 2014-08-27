"""
File for converting Twitter API JSON output to easier-to-use
CSV form 
"""

#json_to_csv.py

import csv
import sys 
import json
import os

def filter_json(old_dict):
    flat_dict = dict()
    
    flat_dict['text'] = old_dict['text']
    flat_dict['time'] = old_dict['created_at']
    flat_dict['geo'] = old_dict['geo']
    flat_dict['source'] = old_dict['source']
    flat_dict['language'] = old_dict['lang']
    flat_dict['screen_name'] = old_dict['user']['screen_name']
    flat_dict['user_location'] = old_dict['user']['location']
    
    return flat_dict


def json_to_array(filename):
    f = open(filename, 'rb')
    
    my_data = []

    for line in f:
        if line.strip():
            my_data.append(filter_json(json.loads(line)))
    
    f.close()

    return my_data


def main():
    
    folder = "./data/"
    outfile = open('game2_tweets.csv', 'wb')
    
    myfields = ['text', 'time', 'geo', 'source', 'language', 
                'screen_name', 'user_location']

    dw = csv.DictWriter(outfile, delimiter=',', fieldnames=myfields)
    dw.writeheader()

    for jsonfile in os.listdir(folder):
        flat_data = json_to_array(folder + jsonfile)
        for line in flat_data:
            dw.writerow({k:(v.encode('unicode_escape') 
                            if isinstance(v, unicode) else v) for k, v in line.items()})

    outfile.close()
    
if __name__ == "__main__":
    main()
