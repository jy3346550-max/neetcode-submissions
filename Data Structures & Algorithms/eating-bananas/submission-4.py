class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        lower, upper = 1, max(piles)
        result = upper
        

        while lower <= upper:
            k = (lower + upper) // 2
            totalTime = 0

            for pile in piles:
                totalTime += math.ceil(float(pile)/k)
            
            if totalTime <= h:
                result = k
                upper = k - 1
            else:
                lower = k + 1
            
            
        
        return result


