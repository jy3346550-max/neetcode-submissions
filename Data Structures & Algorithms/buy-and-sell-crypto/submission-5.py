class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force
        """
        best = 0

        if prices == []:
            return 0
        
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i:
                    if prices[j] > prices[i] and prices[j] - prices[i] > best:
                        best = prices[j] - prices[i]
        
        return best
        """

        max_Profit = 0
        min_Cost = prices[0]

        for cost in range(len(prices)):
            max_Profit = max(prices[cost] - min_Cost, max_Profit)
            min_Cost = min(min_Cost, prices[cost])
        
        return max_Profit



                        

        