'''
Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Examples
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
'''

'''
brute force

因為要買跟賣，所以必定是兩個 index
用兩個 for loop，算出所有買賣點得到的獲利

profit = 0
day_diff = 0
for i in range(len(prices) - 1):
    for j in range(i+1, len(prices)):
        透過 i, j 計算 profit
        每一次比對 profit 是否是最大的，並且要 > 0
            是的話 day_diff = j - i
            否 day_diff = 0

tc : O(N^2)
'''

'''
sliding window

'''
from typing import List

def sliding_window(price : List[int], verbose : bool = True) -> int:
    '''
    ([7,1,5,3,6,4], 5), max :  6 - 1 = 5
    ([7,6,4,3,1], 0), max :  0
    ([7,6,0,3,1,8], 0), max :  8 - 0 = 8
    tc : O(N)
    sc : O(1)
    '''

    max_profit = 0
    left, right = 0, 1 # 雙指標 0 & 1

    # 先考慮右側窗口
    while right < len(price):
        sell_price = price[right]
        # 窗口內的資料更新
        buy_price = price[left]
        sell_price - buy_price
        # 更新答案
        if (sell_price - buy_price) > 0:
            max_profit = max(sell_price - buy_price, max_profit)
        else:
            left = right
            # 考慮左側窗口，優化 profit
            # 1 - 7 < 0, 1 可能是下一個買點，並且並非合法解
        right += 1 # 右窗口增大
        if verbose:
            print(left, right, f'window : {price[left : right]} curr_profit : {max_profit}')
    return max_profit






questions = [
    ([7,1,5,3,6,4], 5),
    # ([7,6,4,3,1], 0),
    # ([7,6,0,3,1,8], 8)
]

for question in questions:
    q, a = question
    for sol in [sliding_window]:
        print(sol(q))
        assert sol(q) == a



