class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        max_val = float('-inf')
        
        rows = len(grid)
        cols = len(grid[0])
        
        # General bounds for any dynamic matrix size
        for r in range(rows - 2):
            for c in range(cols - 2):
                top = grid[r][c] + grid[r][c+1] + grid[r][c+2]
                mid = grid[r+1][c+1]
                bot = grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]

                total = top + mid + bot
                if total > max_val:
                    max_val = total
                    
        return max_val