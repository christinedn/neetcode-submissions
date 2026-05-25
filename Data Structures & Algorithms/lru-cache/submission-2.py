class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node


    # check if the key exist in cache
    # if exist, remove and add it back in so that the MRU (right pointer) is updated
    # if not exist, return -1
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    # if key exist in cache, update the value
    # otherwise, create new node, put it in the cache, update MRU
    # after adding node, must check for capacity 
    # if len(cache) > capacity, remove the LRU
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])   

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru) 
            del self.cache[lru.key]

        
