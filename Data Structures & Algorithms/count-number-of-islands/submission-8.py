class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])
        def dfs(row, col):
            if row < 0 or row >= n or col < 0 or col >= m:
                return 
            if grid[row][col] != "1":
                return

            grid[row][col] = -1

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        islands = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        return islands



        