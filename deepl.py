import requests

from setting import API_KEY, source_lang, target_lang

def translate(s):
    if(s in cache):
        return cache[s]

    params = {
            'auth_key' : API_KEY,
            'text' : s,
            'source_lang' : source_lang,
            "target_lang": target_lang
        }
    response = requests.post("https://api-free.deepl.com/v2/translate", data=params)
    result = response.json()
    cache[s]=result['translations'][0]['text']
    return result['translations'][0]['text']

import os
import pickle
cache={}
if os.path.exists('cache.pkl'):
    with open('cache.pkl', 'rb') as f:
        cache=pickle.load(f)

def saveCache():
    with open('cache.pkl', 'wb') as f:
        pickle.dump(cache, f)
    print(cache)
