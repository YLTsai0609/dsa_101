'''
leetcode 74

Problem Classify 

Is the element be duplicate? Such as 2 of “3” in the metrix

Is the matrix will be empty?

So the problem - given a matrix, with integer, give a target, to check in the matrix or not. Optimal solution will be log(m+n)

Exploring the solution

If we flattern the matrix, for loop to search it will get O(M*N)

Since the array is sorted, we could apply binary search, If we flattern the matrix, apply binary search from two side, it will get O(logM*N)

the first column also match the ascending criteria, we could apply BSearch in 2D flavor, first check the column, then check the rows, It will get O(log(M+N))

Pseudo code

m = len(M), n = len(M[0])

up=0, down=m-1, left=0, right=n-1

def BSearch()

Apply BSearch for M, find a row to digging

For a row, Apply BSearch for n, if exist return true else false

Test case, dryrun, debugging 

debugging
- left is close (included)
- right is open (excluded)
- condition should be left <= right, not left < right, when left == right, we need 1 more search to break the loop
- search condition, left = mid + 1, right = mid - 1, because mid is already been searched

Follow up
- could we use 2D Bsearch?, Yes, O(M+N)
'''
from typing import List

class Solution:
    def searchMatrix_1bs(self, matrix: List[List[int]], target: int, verbose : bool = False) -> bool:
        # O(M*N) version, matrix = 3*4
        m = len(matrix) # 3
        n = len(matrix[0]) # 4
        # For 3x4, m need rounding, target = 13

        left = 0
        right = m * n - 1 # 12
        
        while left <= right:
            # left == right， still need 1 serach
            # 0, 12
            # left = 0, right = 6
            # left = 3, right = 6
            # left = 4, right = 6
            # left = 5, right = 6
            mid = (left + right) // 2
            # mid = 6 --> 1 (6//4), (6 % 2)
            # mid = 3
            # mid = 4
            # mid = 5
            # mid = 5 infinity loop
            curr_y = mid // n 
            # 1
            # 0
            # 1
            # 1
            curr_x = mid % n 
            # 2
            # 3
            # 0
            # 1 
            # matrix[curr_y][curr_x] = 16
            # matrix[curr_y][curr_x] = 7
            # matrix[curr_y][curr_x] = 10
            # matrix[curr_y][curr_x] = 11
            if verbose:
                print(target, matrix[curr_y][curr_x], left, right, mid)
            if target > matrix[curr_y][curr_x]:
                left = mid + 1 # no need to check mid again 
            elif target < matrix[curr_y][curr_x]:
                right = mid - 1 # no need to check mid again 
                # 6
            elif target == matrix[curr_y][curr_x]:
                return True
        return False
    
    def searchMatrix_2bs(self, matrix: List[List[int]], target: int, verbose : bool = False) -> bool:
        m = len(matrix) # 3
        n = len(matrix[0]) # 4
        low,high = 0, m -1
        left, right = 0, n-1
        y_pos = None
        
        while low <= high:
            # 0, 2
            # 0, 0
            mid = (low + high) // 2
            # 1
            # target = 3, matrix[mid][0] = 10, matrix[mid][-1] = 20
            # target = 3, matrix[mid][0] = 1, matrix[mid][-1] = 7
            if verbose:
                print(low, high, mid, matrix[mid][0], matrix[mid][-1])
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                y_pos = mid
                break
                # get y_pos = 0
            elif target < matrix[mid][0]:
                high = mid - 1 
                # high = 0
            elif target > matrix[mid][-1]:
                low = mid + 1
                # low = 2
        # cannot find a row to match the targets
        if y_pos is None:
            return False

        while left <= right:
            # 0, 3
            mid = (left + right) // 2
            # 1
            # target = 3, matrix[0][1] = 3
            if verbose:
                print(y_pos ,left, right, matrix[y_pos][mid])
            if target == matrix[y_pos][mid]:
                return True
            elif target > matrix[y_pos][mid]:
                # perform on right
                left = mid + 1
                # left = 2
                # left = 3
            elif target < matrix[y_pos][mid]:
                right = mid - 1
                # right = 2
        # cannot search the values
        return False



questions = [
    (
         [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False
    ),
    (
         [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60, True
    ),
    (
         [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1, True
    ),
    (
         [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 11, True
    ),
]

for q in questions:
    m, t, ans = q
    sol = Solution()
    for s in ['searchMatrix_1bs','searchMatrix_2bs']:
        assert ans == getattr(sol,s)(m, t)


