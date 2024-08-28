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

dic={
    "關閑": "とじる"
}
cache.update(dic)
saveCache()