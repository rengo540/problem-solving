class Solution(object):
    arr = None
    
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if self.arr is None :
            self.arr = [0 for i in range(n+1)]
            
        if  self.arr[n]:
            return self.arr[n]
        if n<=1 :
            self.arr[n]= 1
            return self.arr[n] 
        
        self.arr[n] =  self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.arr[n]
    


s = Solution()
print(s.climbStairs(5))