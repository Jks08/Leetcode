# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head.next
        prev=head
        while curr:
            s=0
            while curr.val!=0:
                s+=curr.val
                curr=curr.next
            prev.next.val=s
            prev.next.next=curr.next
            prev=curr
            curr=curr.next
        return head.next
