from collections import defaultdict


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        left , right = 0,0
        max_res = 0 
        freq_dic = defaultdict(int)
        while right < n :
            freq_dic[s[right]] +=1
            window_size = right - left +1 
            if window_size - max(freq_dic.values()) > k :
                freq_dic[s[left]] -=1
                left += 1
            else:
                if window_size>max_res :
                    max_res = window_size 
            right +=1

        return max_res
so = Solution()
s = "AABABBA"
k = 1
print(so.characterReplacement(s,k))