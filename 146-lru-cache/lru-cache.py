class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def insert(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
            return 
        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)
        if(len(self.cache)>self.capacity):
            lru_prev = self.tail.prev
            self.remove(lru_prev)
            del self.cache[lru_prev.key]

