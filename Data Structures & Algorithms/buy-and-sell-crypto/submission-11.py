class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         
        mn = prices[0]
        mxp = 0
        for i in range(len(prices)):
            if prices[i] < mn:
                mn = prices[i]
            if prices[i] - mn > mxp:

                mxp = prices[i] - mn
            
        return mxp

            
            
