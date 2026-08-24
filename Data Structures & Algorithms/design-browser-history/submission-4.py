class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.prev = None
        self.next = None
    
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history_head = ListNode(homepage)
        self.cur = self.history_head

    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.cur.next = node
        node.prev = self.cur
        self.cur = node


    def back(self, steps: int) -> str:
        i = 0
        while self.cur.prev and i < steps:
            self.cur = self.cur.prev
            i += 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        i = 0
        while self.cur.next and i < steps:
            self.cur = self.cur.next
            i += 1
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)