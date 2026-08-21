class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}
        for char in range(len(s)):
            countT[t[char]] = 1 + countT.get(t[char], 0)
            countS[s[char]] = 1 + countS.get(s[char], 0)
        
        for letter in countT:
            if countT[letter] != countS.get(letter, 0):
                return False
        return True

    
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # if len(s) != len(t):
        #     return False
        # countT = {}
        # countS = {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # for char in s:
        #     if countS[char] != countT.get(char, 0):
        #         return False
        # return True 

