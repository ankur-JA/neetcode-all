class ListNode:
    def __init__(self,val: int) -> None:
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr != self.tail:
            if index == i:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode
        

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.prev = self.tail.prev
        newNode.next = self.tail

        self.tail.prev.next = newNode
        self.tail.prev = newNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        
        curr = self.head.next
        i = 0
        while curr != self.tail and i < index:
            curr = curr.next
            i += 1
        
        if curr == self.tail and i < index:
            return
            
        newNode = ListNode(val)
        newNode.prev = curr.prev
        newNode.next = curr

        curr.prev.next = newNode
        curr.prev = newNode
            

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next
        i = 0
        while curr != self.tail:
            if index == i:
                node = curr.prev
                node.next = curr.next
                curr.next.prev = node
                return
            curr = curr.next
            i += 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)