"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        fakeHead = ListNode(0)
        cur = fakeHead
        while l1 or l2:
            if not l1:
                cur.next = l2
                break
            elif not l2:
                cur.next = l1
                break
            else:
                if l1.val < l2.val:
                    cur.next = l1
                    cur = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    cur = l2
                    l2 = l2.next
        return fakeHead.next
