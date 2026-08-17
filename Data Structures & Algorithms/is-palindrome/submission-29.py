class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = s
        newS = "".join(c for c in newS if c.isalnum())
        newS = newS.replace(" ", "")
        newS = newS.lower()
        print(newS, newS[::-1])
        

        return newS == newS[::-1]























        









        # newStr = ''
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower()
        # return newStr == newStr[::-1]
        
  