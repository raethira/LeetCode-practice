class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def findValidNeighbors(gene):
            neighbors = []

            for index, char in enumerate(list(gene)):
                ans = list(gene)
                for c in "ACGT":
                    if c != char:
                        ans[index] = c
                        new_gene = "".join(ans)
                        if new_gene in bank:
                            neighbors.append(new_gene)
                
            return neighbors 

        queue = collections.deque([(startGene, 0)])
        seen = {startGene}

        while queue:
            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for neighbor in findValidNeighbors(gene):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, mutations + 1))

        return -1
