"""
leetcode 121
medium
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


def ArrayChallenge(arr):
    # loop onces, get min_price, max_price, tc : O(N), sc : O(1)
    # max_price might be the left
    min_price = arr[0]
    max_price = arr[0]
    max_profit = 0
    for i, price in enumerate(arr):
        if price <= min_price:
            min_price = price
            max_price = 0  # found min price, previous max price is un-reachable
        if price >= max_price:
            max_price = price
        curr_profit = max_price - min_price
        if curr_profit > max_profit:
            max_profit = curr_profit
        # print(min_price, max_price, curr_profit)

    # token :
    key = "5b81frwq0"
    if max_profit > 0:
        return str(max_profit) + ":" + key
    else:
        return "-1" + ":" + key

    # code goes here
    # return arr


# keep this function call here
print(ArrayChallenge(input()))

