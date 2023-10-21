import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        heapq.heapify(nums)
        self.nums = nums
        self.k = k 
        while len(self.nums)>k:
            heapq.heappop(self.nums)
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.nums,val)
        if len(self.nums) > self.k:    
            heapq.heappop(self.nums)
        return self.nums[0]
        
                

# Your KthLargest object will be instantiated and called as such:
nums=[0]
k=2
obj = KthLargest(k, nums)
print(obj.add(-1))
print(obj.add(1))
print(obj.add(-2))
print(obj.add(-4))
print(obj.add(3))