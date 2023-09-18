class Solution(object):
  def containsDuplicate(self, nums):
        dic ={}                  
        for num in nums : 
            
            if dic.__contains__(num):
                return True 
            else : 
                dic[num]=0

        return False 


  