class LRUCache:
    class DoublyLinkedNode:
        def __init__(self, key: int, val: int, prev: DoublyLinkedNode = None, next: BoublyLinkedNode = None):
            self.key = key
            self.val = val
            self.prev = prev
            self.next = next
        
        def __str__(self):
            return f"{self.val}"
        
        def __repr__(self):
            return f"{self.val}"

        def print_list(self):
            print("(" + str(self.key) + ", " + str(self.val) + ")", end=" ")
            if self.next:
                self.next.print_list()

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pairs = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.pairs:
            return -1

        self.update(key)

        return self.pairs[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.pairs:
            self.pairs[key].val = value
            self.update(key)
            return
        
        node = self.DoublyLinkedNode(key, value, self.tail)

        if len(self.pairs) >= self.capacity:
            old_head = self.head
            self.head = self.head.next
            old_head.next = None
            if self.head:
                self.head.prev = None
            self.pairs.pop(old_head.key)
        
        if self.head == None:
            self.head = node
        else:
            node.prev.next = node
        self.tail = node
        
        self.pairs[key] = node

    def update(self, key: int) -> None:
        node = self.pairs[key]

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        node.prev = self.tail
        node.next = None
        self.tail = node