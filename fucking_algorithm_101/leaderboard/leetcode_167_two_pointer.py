"""
1. claasifiy questions
    so let me repeat the questions again if you don't mind
    - all the element in the array is a number
    - the follow a ascending orders
    - the target must be the elements add up, and only 2 elements to achieve that
    - follow up - what if the target could get multiple answer pair?
    - follow up - what if the target doesn't match any awerser pair? (duplicates elements?)
    - return the index, not the actual elements

2. So, for this kind of problem, there are several approaches to solve
    - one of the most simple approach is use 2 for loops, for each loop, we could loop over the array and get almost N*N combinations, 
    once the element add up equal the target number, then we get a solution pair, let's 1
        TC : O(N^2)
        SC : O(1)
    - and since the first approach is kind of brute force, we could build up a hash table for the repeating search, let's say,
    we do first loop to build up a hashtable, key = elements, value = index
    second loop is that, we loop over the numbers, get elements, perform target-element as remind, 
    to check whatever the remind is in the hash-table as key (O(1)), if exist, we get the solution pair
        TC : O(2N) ~ O(N)
        Sc : O(N)
    - the third approach is optimized from sol2, since we need to build a hash table for all elements, it's will cost space complexity O(N)
    However, the elements in the array is sorted, so we could achieve it with space complexity O(1), time complexity O(N), we could try a 
    binary-search-like approach
    we use two pointer, left, right, left starts from zero, right starts from the end of the array, we perform an add operations for two elements, 
    if add up equal to tatget, then solved, if add up less than to that target, we need to make the add up value greater, by the sorted nautre of this questions, 
    left index need to add 1, let's say, left += 1, then we'll get a grater add on values, then perform the checking.
    on the other hand, if thre add up values greater than the targets, we need to make the add up value smaller, by the sorted critiria, we could make
    right index shift to the left, let's say, right -= 1, them perform the checking again, by that, if the solution exist, we may get the solution pair in O(N)

3. pick solution
4. psudo code
5. test-case, simulation and debugging


"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # test case : [2,7,11,15], target = 9
        left, right = 0, len(numbers) - 1
        while left < right:
            # 0 < 3, 0 < 2, 0 < 1, 0=0, break
            # cross over is the fully loop over critirial
            add_up = numbers[left] + numbers[right]
            # 2+15 = 17
            # 2+11 = 13
            # 2+7 = 9
            if target == add_up:
                # there is a index padding I noticed
                return [left+1, right+1] 
            elif target >= add_up:
                # add_up need to grater
                left += 1
            else:
                # left from 3 to 2
                # left from 2 to 1
                right -= 1
        
