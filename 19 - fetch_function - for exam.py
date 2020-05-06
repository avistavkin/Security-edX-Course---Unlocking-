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
        with requests.session() as s:
#            s.head(url)  # do stuff
            _cache[user][url] = s.head(url).content #как альтернатива requests.get
#        _  cache[user][url] = requests.get(url).content
    print("--- %s seconds ---" % round((time.time() - start_time), 4))
    return _cache[user][url]

def did_fetch(user, url):
    if user not in _cache: 
        print ("page ", url, "for user:", user, "is NOT1 cached")
        return
    else:    
        start_time = time.time()
        if url not in _cache[user]:
            print ("page ", url, "for user:", user, "is NOT2 cached")
            return
        else:
            with requests.session() as s:
                _cache[user][url] = s.head(url).content
#            _cache[user][url] = requests.head(url).content #как альтернатива requests.get
#            _cache[user][url] = requests.session(config={'keep_alive': False})
#            requests.config['keep_alive'] = False
            #s = requests.session(config={'keep_alive': False})
            print ("#####_cache[user][url]####\n", _cache) #выводит всё содержимое _cache
 #           _cache[user][url] = requests.get(url).content
        timer = round((time.time() - start_time), 4)
    if timer >= 0.1: print ("page ", url, "for user:", user, "is cached")
    else: print ("page ", url, "for user:", user, "is NOT3 cached")

# for i in range (3):
url1 = "http://ya.ru" 
#input('url...: ')

cache1 = fetch (url1)
   
url1 = "http://ya.ru" 
#input('check url...: ')
user1 = "a17853477"
#input('check user...: ')
did_fetch(user1, url1)
