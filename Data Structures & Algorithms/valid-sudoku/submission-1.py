class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check Rows for invalid boards
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        
        # Check col for invalid col
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in seen:
                    return False
                seen.add(board[j][i])
        
        # Check all 3x3 squares for invalid num
        for square in range(len(board)):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
            
        