import os
import requests
import time

_cache = {}
def fetch(url):
    user = os.environ['USER'] #get current OS user
    print ("user:", user)
    if user not in _cache:
        _cache[user] = {}
    #print ("_cache:", _cache)
    start_time = time.time()
    if url not in _cache[user]:

        _cache[user][url] = requests.get(url).content
    print("--- %s seconds ---" % round((time.time() - start_time), 4))
    return _cache[user][url]

def did_fetch(user, url):
    if user not in _cache: 
        print ("page ", url, "for user ", user, "is NOT1 cashed")
        return
    else:    
        start_time = time.time()
        if url not in _cache[user]:
            print ("page ", url, "for user ", user, "is NOT2 cashed")
            return
        else:
            _cache[user][url] = requests.get(url).content
        timer = round((time.time() - start_time), 4)
    if timer >= 0.1: print ("page ", url, "for user ", user, "is cashed")
    else: print ("page ", url, "for user ", user, "is NOT3 cashed")

# for i in range (3):
url1 = input('url...: ')

cache1 = fetch (url1)
   
url1 = input('check url...: ')
user1 = input('check user...: ')
did_fetch(user1, url1)

#print (cache1)

#for i in range (2):
#    if
#dfhjkdjfhg
