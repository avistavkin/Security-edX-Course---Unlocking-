import os
import requests
import time
import sys # ignore
import pprint 
sys.path.insert(0,'.') # ignore
from Root.fetch import fetch

_cache = {}
def did_fetch(user, url):
    print ("did_fetch(user)", user, sep="")
    print ("did_fetch(url)",url, sep="")
    if user not in _cache: 
        print ("page ", url, "for user", user, "is NOT1 cashed")
        return 0
    else:    
        start_time = time.time()
        if url not in _cache[user]:
            print ("page ", url, "for user", user, "is NOT2 cashed")
            return 1
        else:
            with requests.session() as s:
                _cache[user][url] = s.head(url).content
#            _cache[user][url] = requests.head(url).content
#            s.config['keep_alive'] = False
        timer = round((time.time() - start_time), 4)
    if timer >= 0.1: 
        print ("page ", url, "for user", user, "is cashed")
        return 1
    else: 
        print ("page ", url, "for user", user, "is NOT3 cashed")
        return 1

# for i in range (3):
url1 = "http://www.google.com" 

#cache1 = fetch (url1) 
#print ("!!!!!!!!!!!!cache1:", cache1)

url = "http://www.google.com"
user = "x"
result = did_fetch(user, url)
print ("result:", result)