class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        before, curr = 0, 0
        temp = 1
        while temp < n:
            if prices[curr] <= prices[temp]:
                curr = temp
                temp += 1
            else:
                max_profit += (prices[curr] - prices[before])
                before, curr = temp, temp
                temp += 1
                while temp < n and prices[before] >= prices[temp]:
                    before += 1
                    temp += 1
                    curr = before
        if curr > before:
            max_profit += (prices[curr] - prices[before])
        return max_profit