class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Brute Force
        '''
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                if matrix[i][j] == target:
                    return True
        
        return False
        '''
        
        # Start in top right and scan

        row = 0 
        col = len(matrix[0]) - 1
        num_row = len(matrix)

        while row < num_row and col >= 0:
            if matrix[row][col] > target:
                col -= 1 
            elif matrix[row][col] < target:
                row += 1
            elif matrix[row][col] == target:
                return True
        
        return False