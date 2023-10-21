from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_list = Counter(nums)  
        # count_list = [(-v,k) for k,v in count_list.items()]

        # heapq.heapify(count_list)
        output=[]
        for i in range(k):
            #item = heapq.heappop(count_list)
            output.append()
        print(output)

        return output
arr =[4,1,-1,2,-1,2,3]
s = Solution()
print(s.topKFrequent(arr,2))
