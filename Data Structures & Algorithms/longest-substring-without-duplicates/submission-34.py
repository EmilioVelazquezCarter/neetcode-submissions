class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        alrSeen = set()
        maxLength = 0
        for r in range(len(s)):
            while s[r] in alrSeen:
                alrSeen.remove(s[l])
                l += 1
            
            alrSeen.add(s[r])
            maxLength = max(maxLength, len(alrSeen))
        return maxLength




        # l, r = 0, 0
        # m = 0
        # w = str()
        # while r < len(s):
        #     if s[r] in w:
        #         l += 1
        #     else:
        #         r += 1
        #     w = s[l:r]
        #     m = max(m, len(w))

        # return m
            

