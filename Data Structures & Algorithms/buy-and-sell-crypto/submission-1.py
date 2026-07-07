class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right >= left and right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                if prices[right] - prices[left] > max_profit:
                    max_profit = prices[right] - prices[left]
                right += 1
        
        return max_profit