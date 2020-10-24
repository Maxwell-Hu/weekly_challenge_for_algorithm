class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.lookup = dict()


    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        res = self.lookup[key].val
        self.delete(key)
        self.insert(key, res)
        return res


    def put(self, key: int, value: int) -> None:
        if key not in self.lookup:
            if len(self.lookup) == self.capacity:
                self.delete(self.tail.pre.key)
            self.insert(key, value)
        else:
            self.delete(key)
            self.insert(key, value)


    def insert(self, key, value):
        node = Node(key, value)
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node
        self.lookup[key] = node


    def delete(self, key):
        p = self.lookup[key]
        p.pre.next = p.next
        p.next.pre = p.pre
        self.lookup.pop(key)
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
