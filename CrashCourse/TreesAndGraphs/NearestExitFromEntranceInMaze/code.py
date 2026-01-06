class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == '.'

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        m = len(maze)
        n = len(maze[0])
        queue = collections.deque([(entrance[0], entrance[1], 0)])
        seen = {(entrance[0], entrance[1])}  # hashset

        while queue:
            row, col, steps = queue.popleft()

            if (row in [0, m - 1] or col in [0, n - 1]) and ([row, col] != entrance):
                return steps

            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))

        return -1
