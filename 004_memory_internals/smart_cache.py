import weakref
import sys
import gc

cache = weakref.WeakValueDictionary()

class HeavyObject():
    def __repr__(self):
        return "<Heavy>"

obj = HeavyObject()
cache['key'] = obj

print(f"cache length: {len(cache)}")
print(f"items: {list(cache.items())}")

del obj
gc.collect()

print(f"cache length: {len(cache)}")
print(f"items: {list(cache.items())}")