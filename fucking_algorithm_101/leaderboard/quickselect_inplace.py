"""
Given Ranker (post_1, post_2) return >, < =
0.1M posts, how to rank it?

1. to get TopK - what we need is just partial rank, not fully ranked result.
2. brute force - (p1, p2), (p1, p3), ... (p1, pn) 每一次記錄下最大的，重複k次
    tc O(kn)
    sc O(1)
    bubble sort idea
3. partial sorting - we can use "pivot" (double index version)
    quicksort (but 1 wat only)
    worst case : pivot not help, pick only one element O(N-K)(N)
    average case : divide by 2 

    tc : O(2N) : T = N + N/2 + N/4 + ...
    sc : O(1)
"""

nums = [4, 1, 7, 899, 2, 40]

# high = 5
# low = 0
# pivot = 3
# curr_topk = high (5) - pivot (3) + 1 = 3
# curr_topk == topk, return
# curr_topk > topk (不需要那麼多 topk，繼續選擇)
# curr_topk < topk (需要更多，從pivot-1再選)
# e.g. curr_topk = 2，topk需要往左邊尋找

# [4,2,7,899,40]
# pivot = 2, curr_topk= 5-2+1 = 3
# [899, 40] 找 top2
# if pivot = 40
# [1,2,7,899,40] curr_topk = 1


def quickselect(nums, topk, low, high):
    if len(nums) < topk:
        return nums
    pivot_idx = _partition_in_place(nums, low, high)
    curr_topk = high - pivot_idx + 1
    if curr_topk == topk:
        # no complete sort this case
        return nums[pivot_idx:]

    elif curr_topk < topk:
        # curr_topk = 1
        # topk = 2
        return quickselect(nums, topk, low, pivot_idx - 1)
    else:
        return quickselect(nums, topk, pivot_idx + 1, high)


def quick_sort(A, low, high):
    if low < high:
        pi = _partition_in_place(A, low, high)
        quick_sort(A, low, pi - 1)
        quick_sort(A, pi + 1, high)


def _partition_in_place(nums, low, high, verbose=False) -> int:
    """
    in placed partitioning, two pointer
    https://ithelp.ithome.com.tw/articles/10278644?sc=hot
    
    return pivot position

    pick pivot and swap element to make a pivot
    round 1:
        [4,1,7,899,2,40]
        pivot 4
        i = 1 (1)
        j = 5 (40)
    round 2
        pivot 4
        i = 2 (7) 停止前進
        j = 5
    round 3
        pivot 4
        i = 2 (7)
        j = 4 (2) (停止前進)
    round 4
        pivot 4
        swap i, j
        i = 2 (2)
        j = 4 (7)
        [4,1,2,899,7,40]

    round 5
        pivot 4
        持續 i, j 比較
        i = 3 (899)
        j = 4 (7)
    round 6
        pivot 4
        持續 i, j 比較
        i = 3 (899)
        j = 2 (2)
    round 7
        cross 發生，全部 element 都比過一輪，可以準備插入 Pivot
        swap low, j

    """

    pivot = nums[low]
    i = low + 1
    j = high

    # TODO
    # buggy, i might be greater than array
    # j might be negtive
    while True:
        # 要符合 pivot 定義， 左右各一個指標找到需要交換的元素，必定需要和 pivot 比較
        # 比i, 比j, 比 pivot
        while i <= j and nums[i] <= pivot and i <= len(nums) - 1:
            i += 1
            # i 會停在一個比 pivot 大的值
        while i <= j and nums[j] > pivot and j > 0:
            j -= 1
            # j 會停在一個比 pivot 小的值
        if i <= j:
            # cross 還沒發生， ij的元素交換，符合 pivot
            nums[i], nums[j] = nums[j], nums[i]
        else:
            # crossed, no swaping
            # all element compared
            break
    nums[low], nums[j] = nums[j], nums[low]

    if verbose:
        print(f"current array is {nums} ,pivot is {nums[j]}")
    return j


A = [4, 1, 7, 899, 2, 40]
B = [20, 1, 60, 200, 2, 12, 1, 7]
C = [3, 5, 8, 9, 6, 2]

print(_partition_in_place(A, 0, 5, verbose=True))

# complete sorting is OK
for arr in [A, B, C]:
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)

# but partial sort will be break
print(quickselect(A, 1, 0, len(A) - 1))  # topk=2 will break this
