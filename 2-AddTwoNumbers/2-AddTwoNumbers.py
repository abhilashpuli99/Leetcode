# Last updated: 9/2/2025, 1:44:27 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        carry=total=0
        dummy=ListNode(0)
        head=dummy
        while list1 or list2 or carry:
            total=carry
            if list1:
                total+=list1.val
                list1=list1.next
            if list2:
                total+=list2.val
                list2=list2.next
            num=total%10
            carry=total//10
            dummy.next = ListNode(num)
            dummy=dummy.next
        return head.next
