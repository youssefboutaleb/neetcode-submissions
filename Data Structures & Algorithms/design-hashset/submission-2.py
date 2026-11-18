k=100
class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None
class MyHashSet:

    def __init__(self):
        self.array=[ListNode(-1) for _ in range(k)]

    def add(self, key: int) -> None:
        cur = self.array[key % k]
        while cur.next :
            if cur.next.key == key:
                return 
            cur=cur.next
        cur.next=ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.array[key % k]
        while cur.key != key :
            if cur.next ==None:
                return
            prev = cur
            cur= cur.next
        prev.next=cur.next
        
        

    def contains(self, key: int) -> bool:
        cur = self.array[key % k ]
        while cur.next :
            if cur.key == key :
                return True
            cur=cur.next
        return cur.key == key


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)