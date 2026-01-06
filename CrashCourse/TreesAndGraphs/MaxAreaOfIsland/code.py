class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

        def dfs(row, col):
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy  
                if isValid(next_row, next_col):
                    grid[next_row][next_col] = 0
                    self.area += 1
                    dfs(next_row, next_col)
        
        m = len(grid)
        n = len(grid[0])

        max_area = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
   
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.area = 1
                    grid[i][j] = 0
                    dfs(i, j)
                    max_area = max(max_area, self.area)
                    self.area = 0

        return max_area
