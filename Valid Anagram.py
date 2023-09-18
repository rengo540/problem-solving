import collections 

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {char:0 for char in s }
        for char in s : 
            dic1[char]+=1 
        
        for char in t : 
            if char in dic1:
                dic1[char]-=1
                if dic1[char]==0 :
                    dic1.pop(char)
            else: 
                return False
            
            
        if len(dic1)==0 :
            return True 
        else : 
            return False 

        
s = 'anagram' 
t = 'nagaram'
sol = Solution()
print(sol.isAnagram(s,t))