class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prev = None 
        while head :
            next = head.next 
            head.next = prev 
            prev = head 
            head = next 
        
        curr = prev
        index = 2
        if n == 1 :
            prev = curr.next
        else:    
            while True:
                if index ==n :
                    curr.next = curr.next.next
                    break
                curr = curr.next
                index +=1
            
        
        
        prevv = None 
        while prev :
            next = prev.next 
            prev.next = prevv 
            prevv = prev 
            prev = next 
        return prevv
    

obj = Solution()
head = ListNode(1,ListNode(2,))
res = obj.removeNthFromEnd(head,1)
while res :
    print(res.val)
    res = res.next