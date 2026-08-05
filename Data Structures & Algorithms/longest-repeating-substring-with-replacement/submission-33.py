class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(count.values())
            windowSize = (r - l) + 1
            if windowSize - maxFreq <= k:
                res = windowSize
            else:
                count[s[l]] -= 1
                l += 1
            m = max(0, res)
        return m









        #     if s[l] == s[r]:
        #         r += 1
        #         cl += 1
        #     elif s[l] != s[r] and k > 0:

        #         k -= 1
        #         r += 1
        #         cl += 1
        #     elif s[l] != s[r] and k == 0:
        #         m = max(res, cl)
        #         cl -= 1
        #         l += 1

             
        #     m = max(m, cl)
        #     # print(l, r, cl, m)
        # return m
