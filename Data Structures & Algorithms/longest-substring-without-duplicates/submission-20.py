class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        m = 0
        w = str()
        while r < len(s):


            if s[r] in w:
                l += 1
            else:
                r += 1
            w = s[l:r]
            
            m = max(m, len(w))

        return m
            

