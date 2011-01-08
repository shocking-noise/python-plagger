"""
example

- module: Feed.twitter_search
  config:
    q:
      - query1
      - query2
    page: 2
"""

import simplejson
import urllib2

def twitter_search(config,data):
    data = []
    for q in config['q']:
        for page in xrange(1,config['page']):
            res  = simplejson.loads(urllib2.urlopen('http://search.twitter.com/search.json?q=%s&page=%s' % (q,str(page))).read())
            for tweet in res['results']:
                data.append(q + '\t' + tweet['text'])
    return data
