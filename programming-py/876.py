# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dups_head = head
        head_length = 0
        while dups_head:
            head_length += 1
            dups_head = dups_head.next
        for i in range(head_length//2):
            head = head.next
        return head
