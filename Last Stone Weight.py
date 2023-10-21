import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [i*-1  for i in stones]
        heapq.heapify(stones)
        
        while len(stones)>1:
            first=heapq.heappop(stones)
            second=heapq.heappop(stones)
            if first-second:
                heapq.heappush(stones, first-second)
        if not len(stones):
            return 0
        return -stones[0]
    
    
    
s = Solution()

stones = [3,7,2]

print(s.lastStoneWeight(stones))