'''
Time O(N^{2})

Space O(1)

Stable sort
'''


def bubble_sort(A):
    n = len(A)
    # perform a backward traverse
    for passes in range(n - 1, 0, -1):
        for i in range(passes):
            if A[i] > A[i + 1]:
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp

def bubble_sort_v2(A):
    n = len(A)
    # 從後面回來
    for passes in range(n - 1, 0, -1):
        for i in range(passes):
            # 每次都找最大的
            if A[i] > A[i+1]:
                # swap
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp

A = [3, 5, 8, 9, 6, 2]


print('original array', A)
bubble_sort_v2(A)
print('sorted array', A)
