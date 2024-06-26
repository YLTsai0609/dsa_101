"""
https://leetcode.com/problems/car-pooling/
medium

Naiveloop - tc : O(qN)
DIff - tc : O(q)

假設 : 

1. 只會單向行駛，意思是 index 單調遞增
    如果要折返，也可以，只要每一趟都檢查，即可
2. stops 假設為 1000 站，因為基本上可以無限站
"""


from tracemalloc import stop
from typing import List


class Naiveloop:
    def __init__(self, nums: List[int]) -> None:
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass


class Diff:
    def __init__(self, nums: List[int]) -> None:

        assert len(nums) > 0, "non-valid input array"

        self.diff = [None for _ in range(len(nums))]

        self.diff[0] = nums[0]
        for idx in range(1, len(nums)):
            self.diff[idx] = nums[idx] - nums[idx - 1]

        # # for debug
        # print(self.diff)

    def add(self, index_from: int, index_to: int, val: int) -> None:
        self.diff[index_from] += val
        if index_to + 1 < len(self.diff):
            self.diff[index_to + 1] -= val

    def to_result(self) -> List[int]:
        res = [None for _ in range(len(self.diff))]
        res[0] = self.diff[0]
        for idx in range(1, len(self.diff)):
            res[idx] = res[idx - 1] + self.diff[idx]
        return res


class DiffSol_v2:
    """
		Input: trips = [[2,1,5],[3,3,7]], capacity = 4
        Output: false
    """
    def carPooling(self, trips: List[List[int]], capacity: int, stops=1000) -> bool:
        raw = [0 for _ in range(stops + 1)]
        diff = Diff(raw)

        for tp in trips:
            n_passerengers, index_from, index_to = tp
            index_to -= 1 # [2,1,5] 會在第5站下車
            diff.add(index_from, index_to, n_passerengers)
        
        capacity_over_stops : List[int] = diff.to_result()
        print(capacity_over_stops)
        is_overflow = [capacity_per_stop > capacity for capacity_per_stop in capacity_over_stops]

        if sum(is_overflow) == 0:
            return True
        elif sum(is_overflow) > 0:
            return False
        else:
            raise ValueError('Not Valid Solution')


class DiffSol:
    def carPooling(self, trips: List[List[int]], capacity: int, stops=1000) -> bool:
        """
		Input: trips = [[2,1,5],[3,3,7]], capacity = 4
        Output: false
		"""

        # NOTE: we can loop over the trips to determine max stops instead of giving fix stops 1000
        raw = [0 for _ in range(stops + 1)]

        diff = Diff(raw)

        farest = 0
        for tp in trips:
            n_passengers, index_from, index_to = tp
            if index_to >= farest:
                farest = index_to
            index_to -= 1  # 乘客在 index_to 已經下車
            diff.add(index_from, index_to, n_passengers)

        capacity_over_stops: List[int] = diff.to_result()

        print(capacity_over_stops[:farest])

        for stop_i in range(farest):
            if capacity_over_stops[stop_i] > capacity:
                return False
        return True


if __name__ == "__main__":
    # trips = [[2, 1, 5], [3, 3, 7]]
    # capacity = 5  # true

    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4  # false

    # trips = [[100, 0, 1]]
    # capacity = 1  # false

    # trips = [[9, 3, 4], [9, 1, 7], [4, 2, 4], [7, 4, 5]]
    # capacity = 23  # true
    for c in [DiffSol, DiffSol_v2]:
        _cls = c()
        res = _cls.carPooling(trips=trips, capacity=capacity)
        print(res)
