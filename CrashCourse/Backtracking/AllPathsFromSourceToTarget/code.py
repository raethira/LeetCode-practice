class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def backtrack(curr_node):
            if curr_node == target:
                answer.append(seen[:])
                return
        
            for neighbor in graph[curr_node]:
                if neighbor not in seen:    # You don’t need to check if neighbor not in seen, because the graph is a DAG (Directed Acyclic Graph) and doesn’t contain cycles.
                    seen.append(neighbor)
                    backtrack(neighbor)
                    seen.pop()

        answer = []
        seen = [0]
        target = len(graph) - 1
        
        backtrack(0)

        return answer
