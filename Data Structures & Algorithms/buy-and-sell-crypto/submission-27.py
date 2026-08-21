class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxx = 0
        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxx = max(maxx, profit)
            r += 1
                
                
        return maxx

































        # mn = prices[0]
        # mxp = 0
        # for i in range(len(prices)):
        #     if prices[i] < mn:
        #         mn = prices[i]
        #     if prices[i] - mn > mxp:

        #         mxp = prices[i] - mn
            
        # return mxp

            
            
