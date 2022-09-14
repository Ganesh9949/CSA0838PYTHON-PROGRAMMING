class Solution:
   def solve(self, prices):
      max_profit = 0
      min_stock = float('inf')
      for price in prices:
         max_profit = max(max_profit, price - min_stock)
         min_stock = min(min_stock, price)
      return max_profit
ob = Solution()
print(ob.solve([7,1,5,3,6,4]))
