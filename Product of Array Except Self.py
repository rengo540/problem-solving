class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = 1 
        zero_count = 0
        for num in nums :
            if num != 0 :
                result *= num
            else:
                zero_count +=1 
                
        if zero_count >1 :
            return [0] * len(nums)
        
        arr = []
        for num in nums:
            if num != 0 :
                if zero_count ==1 :
                    arr.append(0)
                else:
                    arr.append(result // num)
            else:
                arr.append(result)
                
        return arr