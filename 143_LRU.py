class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0
        self.cache = dict()


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache[key].prev.next = self.cache[key].next
        self.cache[key].next.prev = self.cache[key].prev
        self.insert_to_head(key)
        return self.cache[key].value


    def put2(self, key: int, value: int) -> None:
        if self.size == self.capacity:
            self.del_tail_node()
            self.size -= 1
        if key not in self.cache:
            self.cache[key] = Node(key, value)
            self.insert_to_head(key)
            self.size += 1
        else:
            self.cache[key].value = value
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev
            self.insert_to_head(key)


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev
            self.insert_to_head(key)
            return
        if self.size == self.capacity:
            self.del_tail_node()
            self.size -= 1
        self.cache[key] = Node(key, value)
        self.insert_to_head(key)
        self.size += 1


    def insert_to_head(self, key):
        self.cache[key].next, self.cache[key].prev = self.head.next, self.head
        self.head.next = self.cache[key]
        self.cache[key].next.prev = self.cache[key]


    def del_tail_node(self):
        del_key = self.tail.prev.key
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        self.cache.pop(del_key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
