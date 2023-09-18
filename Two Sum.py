import collections

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       

        prevMap = {}  

        for i, n in enumerate(nums):
            if n<= target:
                diff = target - n
                if diff in prevMap:
                    return [prevMap[diff], i]
                prevMap[n] = i


S = Solution()
print(S.twoSum([3,2,3],6))