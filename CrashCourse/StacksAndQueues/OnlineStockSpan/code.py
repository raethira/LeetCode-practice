class StockSpanner:
    def __init__(self):
        self.stack = []  # The top of the stack has a format [priceTop, answerTop].

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:   #  While priceTop <= price, add answerTop to ans and pop from the stack.
            ans += self.stack.pop()[1]
        
        self.stack.append([price, ans])
        return ans


        # Answer from https://leetcode.com/problems/online-stock-span/editorial/


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
