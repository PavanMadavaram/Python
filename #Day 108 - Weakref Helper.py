#Day 108 - Weakref Helper
import weakref

class CacheItem:
    pass

items = CacheItem()
proxy = weakref.proxy(items)

print("Proxy works:", isinstance(proxy, CacheItem))