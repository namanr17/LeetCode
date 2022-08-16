class Node:
    def __init__(self, key, value, next_, prev_):
        self.key = key
        self.value = value
        self.next_ = next_
        self.prev_ = prev_

class LRUCache():

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = defaultdict(Node)
        self.head = Node(None, None, None, None)
        self.tail = Node(None, None, None, None)
        
        self.head.next_ = self.tail
        self.tail.prev_ = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.del_(node)
        self.insert_(node)
        
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache.pop(key)
            self.del_(node)
            node.value = value
        else:   node = Node(key, value, None, None)
        
        self.insert_(node)
        self.cache[key] = node
        
        if len(self.cache) > self.cap:
            toDelete = self.head.next_
            self.del_(toDelete)
            del self.cache[toDelete.key]
            
        
    def del_(self, node):
        node.next_.prev_, node.prev_.next_ = node.prev_, node.next_
        
        
    def insert_(self, node):
        lastNode = self.tail.prev_
        lastNode.next_ = node
        node.prev_ = lastNode
        
        node.next_ = self.tail
        self.tail.prev_ = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)