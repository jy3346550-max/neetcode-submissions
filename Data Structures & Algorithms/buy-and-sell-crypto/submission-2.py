class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        best = 0

        if prices == []:
            return 0
        
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i:
                    if prices[j] > prices[i] and prices[j] - prices[i] > best:
                        best = prices[j] - prices[i]
        
        return best

                        

        