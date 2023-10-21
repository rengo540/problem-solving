class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result ={}
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word in result:
                result[sorted_word].append(word)
            else:
                result[sorted_word] = [word]
        
        return list(result.values())
    
    
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))