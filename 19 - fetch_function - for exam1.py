#вот этот файлик пока ближе всего...







import os
import requests
import time
import sys # ignore
import pprint 
sys.path.insert(0,'.') # ignore
from Root.fetch import fetch


#def did_fetch(user, url):
#    pass #return if url has been fatched by user

_cache = {}
def fetch(url):
    user = "alice"
    #os.environ['USER'] #get current OS user
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
    print ("did_fetch(user)", user, sep="")
    print ("did_fetch(url)",url, sep="")
    env_var = os.environ 

# Print the list of user's 
# environment variables 
    print("User's Environment variable:") 
    pprint.pprint(dict(env_var), width = 1) 
    if user not in _cache: 
        print ("page ", url, "for user", user, "is NOT1 cashed")
        return 0
    else:    
        start_time = time.time()
        if url not in _cache[user]:
            print ("page ", url, "for user", user, "is NOT2 cashed")
            return 0
        else:
            _cache[user][url] = requests.get(url).content
        timer = round((time.time() - start_time), 4)
    if timer >= 0.1: 
        print ("page ", url, "for user", user, "is cashed")
        return 1
    else: 
        print ("page ", url, "for user", user, "is NOT3 cashed")
        return 0

# for i in range (3):
url1 = "http://www.google.com" 
#input('url...: ')

cache1 = fetch (url1)
   
url = "http://www.google.com"
user = "x"
result = did_fetch(user, url)
print ("result:", result)