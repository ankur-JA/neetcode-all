# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr1 = list1
        curr2 = list2
        while curr1:
            stack.append(curr1.val)
            curr1 = curr1.next
        
        while curr2:
            stack.append(curr2.val)
            curr2 = curr2.next
        

        stack.sort()
        tmp = ListNode(-1)
        head = tmp
        for num in stack:
            new_node = ListNode(num)
            tmp.next = new_node
            tmp = new_node
        
        return head.next