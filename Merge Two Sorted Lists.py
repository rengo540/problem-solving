# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current1 =list1
        current2 =list2
        head = ListNode()
        prev = head

        while current1  and current2 :

            if current1.val < current2.val :
                prev.next = current1
                current1 = current1.next 
            else:
                prev.next = current2
                current2 =current2.next 
            prev = prev.next

        prev.next = current1 or current2


        return head.next





