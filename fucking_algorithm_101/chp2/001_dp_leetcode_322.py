"""
coinChange
medium
"""

# recursion
# base case amount = 0, n_coins = 0
# res = float('inf')
# amount = 11
# for coin in coin_choince:
# 哪一個最少?
# res = min(res, sub_problem + 1)
# 畫出遞迴樹
# 每次有 k 個選擇
# 如果 amount 有 N，最遭要選 N 次
# tc : O(k^n)
# sc : O(1)

from typing import List


# 較難 debug
def coin_change_recursion(coins: List[int], amount: int) -> int:
    # top-down
    def dp(coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        n_coin_counts = float("inf")
        for choice in coins:
            sub_problem: int = dp(coins, amount - choice)
            # 無解時跳過
            if sub_problem == -1:
                continue
            n_coin_counts = min(n_coin_counts, sub_problem + 1)
            # base case 給 0，但是就是剛好找完硬幣的意思，每個面額會換到不同的硬幣數量，找最少的
        return n_coin_counts if n_coin_counts != float("inf") else -1

    return dp(coins, amount)


# top-down
# 建立 cached
# tc O(kn), k個選擇都要跑，但遇到 cached , O(1), 至多跑 kn 個
# sc O(n)
def coin_change_recursion_with_cache(coins: List[int], amount: int) -> int:
    # Suppose amount = 6, coins = [5,1]
    cached = {}
    # [float('-inf'), ...] seven elements
    cached[0] = 0

    def recursive_with_cached(coins, amount, cached, verbose=False):
        if amount in cached.keys():
            return cached[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        n_coin_counts = float("inf")
        for choice in coins:
            # 5,1
            sub_problem: int = recursive_with_cached(coins, amount - choice, cached)
            # level = 1 [6-5, 6-1]
            # level = 2, [6-5-5, 6-5-1]
            # 無解時跳過
            if sub_problem == -1:
                continue
            n_coin_counts = min(n_coin_counts, sub_problem + 1)
            # base case 給 0，但是就是剛好找完硬幣的意思，每個面額會換到不同的硬幣數量，找最少的
        cached[amount] = n_coin_counts if n_coin_counts != float("inf") else -1
        if verbose:
            print(amount, n_coin_counts)
        return cached[amount]

    return recursive_with_cached(coins, amount, cached)


# bottom-up
def coin_change_iteration_with_cached(
    coins: List[int], amount: int, verbose: bool = False
) -> int:
    """
    [5,2,1], 5 --> 1
    """
    cached = [float("inf")] * (amount + 1)
    cached[0] = 0

    # 一路跑到給定的零錢值 amount
    for i in range(1, len(cached)):
        # 所有選擇都要被窮舉
        for choice in coins:
            # i - choice 等於找錢的量
            if i - choice < 0:
                continue
            else:
                cached[i] = min(cached[i], 1 + cached[i - choice])
            # dp[1] 會掉到 dp[0], dp[2] 會掉到 dp[0], dp[3] 會掉到 dp[1], dp[4] 會掉到 dp[2], dp[5] 會掉到 dp[0]
            # 照理來說要看到 choice = 5
            if verbose:
                print(f"i= {i}, amount : {amount}, choice : {choice}  {cached}")
    return -1 if cached[amount] == float("inf") else cached[amount]


questions = [
    ([5, 2, 1], 1, 1),
    ([5, 2, 1], 2, 1),
    ([5, 2, 1], 3, 2),
    ([5, 2, 1], 4, 2),
    ([5, 2, 1], 5, 1),
    ([2], 3, -1),
]

for coins, amount, n_coin_count in questions:
    print(coins, amount, n_coin_count)
    for _func in [
        coin_change_recursion,
        coin_change_recursion_with_cache,
        coin_change_iteration_with_cached,
    ]:
        # print(_func(coins, amount))
        pred = _func(coins, amount)
        assert (
            pred == n_coin_count
        ), f"expected {n_coin_count}, got : {pred}, func : {_func.__name__}"
