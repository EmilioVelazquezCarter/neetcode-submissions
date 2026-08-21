class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) -1

        while l < r:
            while l < r and not s[l].isalnum(): 
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True






























        # l, r = 0, len(s) -1

        # while l < r:
        #     while l < r and not s[l].isalnum(): 
        #         l += 1
        #     while l < r and not s[r].isalnum():
        #         r -= 1
        #     if s[l].lower() != s[r].lower():
        #         return False
        #     l += 1
        #     r -= 1
        # return True
















        # # newS = s
        # # newS = "".join(c for c in newS if c.isalnum())
        # # newS = newS.replace(" ", "")
        # # newS = newS.lower()
        # # print(newS, newS[::-1])
        

        # # return newS == newS[::-1]



