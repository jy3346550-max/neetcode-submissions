class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            cur = stones[len(stones)-1] - stones[len(stones)-2]
            stones.pop(), stones.pop()
            if cur != 0:
                stones.append(cur)
        
        if stones:
            return stones[0]
        else:
            return 0
        