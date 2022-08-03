"""
[On average] Time O(N logN)
[Worst Case] Time O(N^2) reduce to single linked list

Space O(1)

"""


def quick_sort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quick_sort(A, low, pi - 1)
        quick_sort(A, pi + 1, high)


def partition(A, low, high):
    pivot = A[low]
    i = low + 1
    j = high
    while True:
        while i <= j and A[i] <= pivot:
            # not crossed, and A[i] <= pivot, keep traversing
            i += 1
        while i <= j and A[j] > pivot:
            # not crossed, and A[j] <= pivot, keep traversing
            j -= 1
        if i <= j:
            # swap i, j for matching the definition of pivot
            A[i], A[j] = A[j], A[i]
        else:
            # j just cross i
            # we find the position to swap pivot
            break
    A[low], A[j] = A[j], A[low]
    return j


A = [3, 5, 8, 9, 6, 2]

print("original array", A)
quick_sort(A, 0, len(A) - 1)
print("sorted array", A)

B = [20, 1, 60, 200, 2, 12, 1, 7]

quick_sort(B, 0, len(B) - 1)

print(B)

C = [4, 1, 7, 899, 2, 40]

quick_sort(C, 0, len(C) - 1)
print(C)
