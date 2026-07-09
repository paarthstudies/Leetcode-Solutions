class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0
        self.myhash = {}
        self.capacity = capacity

    def _remove(self, node: Node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        self.length -= 1

    def _insert(self, node: Node):
        firstnode = self.head.next
        self.head.next = node
        node.next = firstnode
        firstnode.prev = node
        node.prev = self.head
        self.length += 1
            
    def get(self, key: int) -> int:
        if key not in self.myhash:
            return -1
        target = self.myhash[key]
        self._remove(target)
        self._insert(target)
        return target.value
            
    def put(self, key: int, value: int) -> None:
        if key in self.myhash:
            self._remove(self.myhash[key])
        new_node = Node(key, value)
        self._insert(new_node)
        self.myhash[key] = new_node
        if self.capacity < len(self.myhash):
            temp = self.tail.prev
            self._remove(temp)
            del self.myhash[temp.key]
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value) if self.length == 0:
            # self.head = new_node
            # self.tail = new_node