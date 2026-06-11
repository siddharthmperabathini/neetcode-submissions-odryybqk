# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        start = head
        if not head.next:
            return None
        while temp:
            count += 1
            temp = temp.next

        if count == n:
            return start.next
        count -= n
        for i in range(count - 1):
            head = head.next
        head.next = head.next.next
        return start