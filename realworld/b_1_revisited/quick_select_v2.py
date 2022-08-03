from typing import List, Union


def partition(arr: List[int], low: int, high: int) -> int:
    """
    double index version
    """
    pivot = arr[low]
    i = low
    j = high
    while True:

        # To find a candidate to swap i, j
        while i <= j and arr[i] <= pivot:
            i += 1

        # To find a candidate to swap i, j
        while i <= j and arr[j] > pivot:
            j -= 1

        # match definition of pivot, swap i, j
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    # match definition of pivot, swap pivot, j
    arr[low], arr[j] = arr[j], arr[low]

    return j


arr = [54, 78, 63, 92, 45, 86, 15, 28, 37]

print(partition(arr, 0, len(arr) - 1))
