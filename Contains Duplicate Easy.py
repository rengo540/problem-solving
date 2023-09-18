class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        #dic = {num:   for num in nums }
        #dic = {num:0 for num in nums}
        dic ={}                  
        for num in nums : 
            
            if dic.__contains__(num):
                return True 
            else : 
                dic[num]=0

        return False 



S = Solution()
print(S.containsDuplicate([1,2,3])) 