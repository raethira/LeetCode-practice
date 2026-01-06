from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.sum = 0
        self.length = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.sum += val
        self.length += 1

        while self.length > self.size:
            popped = self.queue.popleft()
            self.sum -= popped
            self.length -= 1

        return self.sum / self.length
        
        # Time: O(1)
        # Space: O(size)




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
