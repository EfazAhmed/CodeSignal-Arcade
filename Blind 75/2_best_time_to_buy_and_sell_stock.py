class Solution(object):
    def maxProfit(self, prices):
        
        p1 = 0
        p2 = p1 + 1
        
        max_profit = 0
        
        while p1 < len(prices) and p2 < len(prices):
            if prices[p2] - prices[p1] > max_profit:
                max_profit = prices[p2] - prices[p1]
            elif prices[p2] < prices[p1]:
                p1 = p2
            p2 += 1
            
        return max_profit
                    