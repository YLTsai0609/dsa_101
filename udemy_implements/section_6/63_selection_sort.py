'''
Time O(N^{2})

Space O(1)

Unstable sort
'''


def selection_sort_v2(A):
    '''
    for i in range(n):
        1. pick minimum
        2. place at left
    A = [3, 5, 8, 9, 6, 2]
        1. [2, 5, 8, 9, 6, 3]
        2. [2, 3, 8, 9, 6, 5]
    '''
    # 每一輪比上每一輪 +1, 設當前 minimum 為 pos
    # A[i], A[pos] 互換
    n = len(A)
    for i in range(n-1):
        pos = i # 假設 A[pos] = 3 是最小值
        for j in range(i+1, n):
            # 找到新的最小值，並取代 
            # A[6] = 2, pos = 6
            if A[j] < A[pos]:
                pos = j
        
        # swap A[pos] to A[i]
        # [2, 5, 8, 9, 6, 3]
        tmp = A[i]
        A[i] = A[pos]
        A[pos] = tmp


A = [3, 5, 8, 9, 6, 2]


print('original array', A)
selection_sort_v2(A)
print('sorted array', A)
