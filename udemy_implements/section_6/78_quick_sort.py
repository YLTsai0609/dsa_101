"""
[On average] Time O(N logN)
[Worst Case] Time O(N^2) reduce to single linked list, every pivot is just next to low or high

Space O(1)

"""

from typing import List

def quick_sort(A : List[int], low : int, high : int) -> None:
    if low < high:
        pi = partition(A, low, high)
        quick_sort(A, low, pi-1)
        quick_sort(A, pi+1, high)

def partition(A : List[int], low : int, high : int) -> int:
    '''
    output : the left should be smaller than pivot, the right should be larger
    '''
    # A = [3, 5, 8, 9, 6, 2]
    pivot = A[low] # hypoetherically, pivot = A[1] = 3
    i = low + 1
    j = high
    
    while True:
        while i <= j and A[i] <= pivot:
            # not crossed, A[i] <= pivot match definition, do nothing
            i+=1
        while i <= j and A[j] > pivot:
            # not crossed, A[j] > pivot match definition, do nothing
            j-=1
        
        if i<=j:
            # meet A[i] > pivot or A[j] < pivot, swap i, j, to match the definition
            A[i], A[j] = A[j], A[i]
        else:
            # crossed, all travered
            break
    # pivot at A[low]
    # A[j] is the smaller
    # A[i] is the greater
    # we swap pivot, A[j] to put the pivot at right position
    # check 75_quick_sort.md
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
