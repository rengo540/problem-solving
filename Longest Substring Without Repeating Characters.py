class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = []
        right=0 
        left = 0
        max = 0
        print(len(s))
        while left < len(s):
            if right < len(s):
                if s[right] in arr:
                    left +=1
                    right = left  
                    arr = []
                else:
                    arr.append(s[right])
                    if len(arr) > max:
                        max = len(arr)
                    right +=1                
            else:
                left +=1 
                right = left 
                arr = []
                
        return max
    

so = Solution()
s = "pwwkew"

print(so.lengthOfLongestSubstring(s))