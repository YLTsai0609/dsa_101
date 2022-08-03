def qselect(arr, k):
    if len(arr) <= k:
        return arr

    pivot = arr[-1]
    right = [pivot] + [e for e in arr[:-1] if e >= pivot]
    curr_topk = len(right)

    if curr_topk == k:
        return right

    if curr_topk > k:
        qselect(right, k)
    else:
        left = [e for e in arr[:-1] if e < pivot]
        # print(len(arr), k, curr_topk, right)
        return qselect(left, k - curr_topk) + right


C = [4, 1, 7, 899, 2, 40]

print(qselect(C, 4))

