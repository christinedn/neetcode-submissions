class Node:
    def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev =  None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.lru, self.mru = Node(), Node()
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def add(self, node):
        temp = self.mru.prev 
        temp.next = node
        node.prev = temp
        self.mru.prev = node
        node.next = self.mru


    def remove(self, node):
        first = node.prev 
        second = node.next
        first.next = second
        second.prev = first

        
    def get(self, key: int) -> int:
        if key in self.cache:
            temp = self.cache[key]
            self.remove(self.cache[key])
            self.add(temp)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.add(newNode)
        # check if num already exist in cache. ??
        self.cache[key] = newNode
        if len(self.cache) > self.cap:
            # only remove from dict if the capacity is exceeded
            lruNode = self.lru.next
            del self.cache[lruNode.key]
            self.remove(lruNode)
            # then you can add new key, make new key mru
        
