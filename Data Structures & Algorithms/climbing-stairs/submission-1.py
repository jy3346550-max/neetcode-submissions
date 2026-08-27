class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Recursion
        '''
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        return (self.climbStairs(n-1) + self.climbStairs(n-2))
        '''

        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        
        return one