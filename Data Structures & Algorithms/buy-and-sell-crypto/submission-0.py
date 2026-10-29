class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        max_value = 0
        for price in prices:
            if price < min_value:
                min_value = price
            elif price - min_value > max_value:
                max_value = price - min_value
        
        return max_value
        