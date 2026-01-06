class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        queue = collections.deque([start])
        seen = {start}

        while queue:
            i = queue.popleft()

            if arr[i] == 0:
                return True

            for neighbor in [i + arr[i], i - arr[i]]:
                if neighbor not in seen and 0 <= neighbor and neighbor < len(arr):
                    seen.add(neighbor)
                    queue.append(neighbor)

        return False
