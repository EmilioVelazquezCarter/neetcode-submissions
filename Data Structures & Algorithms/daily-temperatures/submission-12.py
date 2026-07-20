class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ccl = []
        for i in range(len(temperatures)):
            temp = temperatures[i]
            x = i + 1
            while (len(temperatures)) > x and temperatures[x] <= temp:
                x += 1
            if x < len(temperatures):
                ccl.append(x - i)
            else:
                ccl.append(0)
            

        return ccl
