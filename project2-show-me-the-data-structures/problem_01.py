from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity = 5):
        if capacity <= 0:
            raise ValueError("Error: Cache capacity must be greater than 0.")
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            # Move the key to the end to indicate it was recently used
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1

    def set(self, key, value):
        # If the key already exists in the cache, remove the value and move it to the end.
        if key in self.cache:
            self.cache.pop(key)
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last = False)
        self.cache[key] = value

    # support print cache
    def __str__(self):
        out_string = ''
        for key in self.cache:
            out_string += str(key) + '->'
        out_string += 'End'

        return out_string


## Test cases
# A cache with a capacity of 5
print("===== Test case #1 =====")

cache_01 = LRU_Cache(5)
cache_01.set(1, 1)
cache_01.set(2, 2)
cache_01.set(3, 3)
cache_01.set(4, 4)
print("cache_01: ", cache_01)

print("# returns 1 - cache_01.get(1):", cache_01.get(1))
print("cache_01: ", cache_01)

print("# returns 2 - cache_01.get(2):", cache_01.get(2))
print("cache_01: ", cache_01)

print("# returns -1 - cache_01.get(5):", cache_01.get(5))
print("cache_01: ", cache_01)

cache_01.set(5,6)
cache_01.set(6,6)
print("cache_01 - cache_01.set(5), cache_01_set(6): ", cache_01)

print("# returns -1 - cache_01.get(3):", cache_01.get(3))
print("cache_01: ", cache_01)


# A new cache with a capacity of 3
print("===== Test case #2 =====")
cache_02 = LRU_Cache(3)
cache_02.set(1, 1)
cache_02.set(2, 2)
cache_02.set(3, 3)
print(" cache_02:", cache_02)

cache_02.set(1, 10)
print(" cache_02:", cache_02)

print("#returns 2:", cache_02.get(2))
print(" cache_02:", cache_02)

# A cache with a capacity of 0
print("===== Test case #3 =====")
try:
    cache_03 = LRU_Cache(0)
    print("Capacity of cache is ", cache_03.capacity)

    # Should raise an exception
    cache_03.set(1, 1)
except ValueError as ve:
    print(ve)
