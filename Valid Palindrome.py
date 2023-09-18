import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sentance =  re.sub('[^A-Za-z0-9]+','',s)
        sentance =  sentance.lower()
        if(len(sentance)==1):
                return True  
        left = 0 
        right = len(sentance) - 1  
        
        while(left < right):
            if(sentance[left] == sentance[right]):
                left += 1 
                right -= 1 
            else :
                return False 
        return True 