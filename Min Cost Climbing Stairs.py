
class Solution(object):
    arr = None

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        self.arr = [0 for i in range(n+1)]
        #cost.append(0)
        return self.minCostBottonUp(cost)
    def minCost(self,cost ,n):
            
        if  self.arr[n]:
            return self.arr[n]
        if n<=1 :
            return cost[n]
        
        self.arr[n] = min(self.minCost(cost,n-1),self.minCost(cost,n-2))+cost[n]
        return self.arr[n]
    
    def minCostBottonUp(self,cost):
        self.arr[0]=cost[0]
        self.arr[1]=cost[1]
        for i in range(2,len(cost)):
            self.arr[i]= min(self.arr[i-1],self.arr[i-2])+cost[i]
        
        return min(self.arr[len(cost)-1],self.arr[len(cost)-2])
        
    
s = Solution()
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))