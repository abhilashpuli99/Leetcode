# Last updated: 9/2/2025, 1:41:18 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        if head is None:
            return 0
        temp=head
        value=""
        while temp:
            value+=str(temp.val)
            temp=temp.next
        return int(value,2)