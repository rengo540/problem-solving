#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        #find middle 
        iter, middle = head,head
        while iter.next and iter.next.next:
            middle = middle.next
            iter = iter.next.next 
            
        
        #reverse the second half
        prev = None
        curr= middle.next
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        middle.next = None
        head1 ,head2 = head , prev
        while head2:
            next = head1.next
            head1.next = head2
            head1 = head2
            head2 = next
                        
                
        return head
obj = Solution()
head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
res = obj.reorderList(head)
while res :
    print(res.val)
    res = res.next