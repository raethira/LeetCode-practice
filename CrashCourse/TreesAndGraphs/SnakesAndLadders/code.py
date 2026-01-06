class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        def boustrophedonMapping(n):
            chess = [0] * (n * n + 1) 
            label = 1
            columns = range(n)

            for i in range(n-1, -1, -1):
                for j in (columns):
                    chess[label] = (i, j)
                    label += 1
                columns = columns[::-1]

            return chess

        n = len(board)
        mapping = boustrophedonMapping(n) 
    
        queue = collections.deque([(1, 0)])
        seen = {1}

        while queue:
            curr, rolls = queue.popleft()
 
            if curr == n * n:
                return rolls

            for next_curr in range(curr + 1, min(curr + 6, n * n) + 1):
                next_row, next_col = mapping[next_curr]

                if board[next_row][next_col] != -1:                    
                    next_curr = board[next_row][next_col]

                if next_curr not in seen:    
                    seen.add(next_curr)
                    queue.append((next_curr, rolls + 1))
        
        return -1
