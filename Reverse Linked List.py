class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        while current != None :
            next = current.next 
            current.next = prev
            prev = current 
            current = next 
        head = prev
        return head


head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))


s = Solution()
res = s.reverseList(head)

while res != None:
    print(res.val)
    res = res.next
