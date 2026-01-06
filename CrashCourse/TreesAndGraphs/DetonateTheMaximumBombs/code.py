class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
     
        def dfs(node):
            seen.add(node)
            count = 1
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    count += dfs(neighbor)

            return count

        n = len(bombs)
        graph = collections.defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                x_i = bombs[i][0]
                y_i = bombs[i][1]
                r_i = bombs[i][2]

                x_j = bombs[j][0]
                y_j = bombs[j][1]
                r_j = bombs[j][2] 

                if math.sqrt(pow(x_j - x_i , 2) + pow(y_j - y_i , 2)) <= r_i:
                    graph[i].append(j)
        
                if math.sqrt(pow(x_j - x_i , 2) + pow(y_j - y_i , 2)) <= r_j:
                    graph[j].append(i)

        ans = 0

        for i in range(n):
            seen = set()
            ans = max(ans, dfs(i))    

        return ans
