# Comparision based sorted algorithms

which compares elements.

| Algorithms | Best Case | Average Case | Worst Case | Space | Stable | Note |
|------------|-----------|--------------|------------|-------|--------|------|
| Selection Sort      | $O(N^2)$     | $O(N^2)$        |     $O(N^2)$       |   $O(1)$    |  No   |  if input array is already sorted, the algorithm will not know that. git $O(N^2)$   |
| Insertion Sort      | $O(N)$     | $O(N^2)$        |     $O(N^2)$       |   $O(1)$    |  Yes   |  the algorithm will not take a lot of time if the array is sorted   |
| Bubble Sort      | $O(N)$     | $O(N^2)$        |     $O(N^2)$       |   $O(1)$    |  Yes   |  the algorithm will not take a lot of time if the array is sorted   |
| Shell Sort      | $O(N log N)$     | $O(N log N)$        |     $O(N^2)$       |   $O(1)$    |  No   |     | 
| Merge Sort      | $O(N log N)$     | $O(N log N)$        |     $O(N log N)$       |   $O(N)$    |  Yes   |  divide and conquer approach   |
| Quick Sort      | $O(N log N)$     | $O(N log N)$        |     $O(N^2)$       |   $O(N)$    |  No   |  divide and conquer approach   |
| Heap Sort      | $O(N log N)$     | $O(N log N)$        |     $O(N log N)$       |   $O(1)$    |  No   |     |

# Indexed based algorithms

| Algorithms | Best Case | Average Case | Worst Case | Space | Stable | Note |
|------------|-----------|--------------|------------|-------|--------|------|
| Count Sort      | $O(N)$     | $O(N)$        |     $O(N)$       |   $O(N)$    |  Yes   |  if the maximum elements is too big, we are using a lot of memory.   |
| Bucket / Bin Sort      | $O(N)$     | $O(N^2)$        |     $O(N^2)$       |   $O(N)$    |  Yes   |   |
| Radix Sort      | $O(N)$     | $O(N)$        |     $O(N)$       |   $O(N)$    |  Yes   |   |


1. selection sort

```python
# 每一輪找到 minimum，並且擺在當前的最左邊
for i in range(n-1):
    i = pos # A[pos] 假設為最小值
    for j in range(i+1, n):
        # 從剩下的找最小值，找到的話，指定為 pos
        if A[j] < A[pos]:
            pos = j 
    # swap A[pos], A[i]
```


2. bubble sort

```python
# 每一輪找到最大的，放右邊，比較的方式是把剩下的兩兩相比
for passed in range(n-1. 0, -1):
    for i in range(passed):
        if A[i] > A[i+1]:
            # swap
    # 左邊和右邊比，如果左邊比右邊大，就互相 swap
```