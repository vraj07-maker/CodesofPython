# Declare a 2D array as a list of lists using [] and commas
a = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

class Solution:
    def hourglass(self, arr):
        max_val = float('-inf')
        
        # Loop through row indices 0 to 3
        for r in range(4):
            # Loop through column indices 0 to 3
            for c in range(4):
                top = arr[r][c] + arr[r][c+1] + arr[r][c+2]
                mid = arr[r+1][c+1]
                bot = arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2]
                
                total = top + mid + bot
                
                # Update max_val when a larger total is found
                if total > max_val:
                    max_val = total
                    
        return max_val

sol = Solution()
print(sol.hourglass(a))  # Output: 19