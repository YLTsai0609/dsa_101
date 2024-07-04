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


# Review

[fast way - use viz](https://visualgo.net/en/sorting?slide=8)

1. selection sort

```python
A = [8,5,20,19,24]
n = len(A)
# 每一輪找到 minimum，並且擺在當前的最左邊
for i in range(n-1):
    i = pos # A[pos] 假設為最小值
    for j in range(i+1, n):
        # 從剩下的找最小值，找到的話，指定為 pos
        if A[j] < A[pos]:
            pos = j # 每一輪都找到當下最小值的 index
    A[pos], A[j] = A[j], A[pos] # swap
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

3. merge sort

```python
# devided and conquer (by a tree tech)
# 一路二分法往下切，切到只剩一個 element (一定是 sorted，因為只有一個 element)
# bottom-up : merge function
# 雙指標排序好每一次 merge

def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2  # we need integer to index list
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

#TODO
def merge(A, left, mid, right):
    i = left
    j = mid + 1
    k = left
    B = [0] * (right + 1)
    while i <= mid and j <= right:
        if A[i] < A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1
    while i <= mid:
        B[k] = A[i]
        i += 1
        k += 1
    while j <= right:
        B[k] = A[j]
        j += 1
        k += 1
    for x in range(left, right + 1):
        A[x] = B[x]


```

4. quick sort

```python

A = [3, 5, 8, 9, 6, 2]

def quick_sort(A : List[int], low : int, high : low) -> None:
    '''
    best : O(log2N)
    worst : O(N)
    '''
    if low < high:
        # Tree Splits
        pi = partition(A, low, high)
        quick_sort(A, low, pi-1)
        quick_sort(A, pi+1, high)

def partition(A : List[int], low : int, high : int) -> int:
    '''
    tc : O(N)
    sc : O(1)
    '''
    
    pivot = A[low] # hypetherically
    i = low + 1
    j = high

    # swap i,j based on pivot relation
    while True:
        while i <= j and A[i] <= pivot:
            i += 1  
        while i <= j and A[j] > pivot:
            j -= 1
        
        if i < j:
            # find the element we need to swap
            A[i], A[j] = A[j], A[i]
        else:
            break    
    # A[i], A[j] now match the def
    # swap A[low], A[j], j is the pivot position
    A[low], A[j] = A[j], A[low]
    return j
```