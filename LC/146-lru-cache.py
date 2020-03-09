# BEST SOLUTION -> OrdererDict from collections
from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = deque()
        self.entries = {}
        self.capacity = capacity

    def __rearrage(self, key):
        self.cache.remove(key) # O(n)
        self.cache.append(key)

    def get(self, key: int) -> int:
        if key not in self.entries:
            return - 1

        self.__rearrage(key)

        return self.entries[key]


    def put(self, key: int, value: int) -> None:
        if key in self.entries:
            self.entries[key] = value
            self.__rearrage(key)
            return

        if len(self.entries) == self.capacity:
            least_key = self.cache.popleft()
            del self.entries[least_key]

        self.entries[key] = value
        self.cache.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)