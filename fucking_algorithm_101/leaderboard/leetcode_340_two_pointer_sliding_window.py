'''
leetcode 360

Problem Classify & Edge Case

A string, interger K, what if interger K is greater than the string lens?

Solutions

We use 2 pointer with 2 for loop to loop over the string, let's say left and right —> get all combination —> check the substring match the K distinct values or not by build up a hash table for each combination 

TC : O(N^3)

SC : O(N) 

Another thought is 2 pointer but sliding window approach, left and right starts from 0 and 1 —> get substring

check match criteria, if not, expand the window by right +=1 

if match criteria, record length, shrinkage the window by left +=1

once the loop is over, we’ll explore all combinations and get minimum length

TC : O(N)

SC : O(1)

Pseudo code 10/16

left=0, right=0, window = defaultdict(int) curr_substring_length = 0

while right < len(s) (Expanding window)

c = s[right]

window[c] += 1

debug message 

while left < right AND (window need shrinking)

 d = s[left]

window[d] -= 1

curr_substring_length = max(curr_substring_length, right-left +1）
'''
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int, verbose : bool = True) -> int:
        left = 0
        right = 0 # s[left:right] is include, exclude
        window = defaultdict(int)
        curr_sub_length = 0
        # k = 1
        # start expanding window and find feasible solutions
        # s = abee
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            # NOTE: when the solution become in-feasible, shrink the window
            while left < right and len(window.keys()) > k:
                d = s[left]
                left += 1
                if d in window.keys():
                    window[d] -= 1
                    if window[d] == 0:
                        del window[d]
                    # window = {'b':2,'c':1}
            curr_sub_length = max(curr_sub_length, right - left + 1
            ) # update the solution is no need in the sub while loops
            # w = {'a':1}, 1
            # w = {'a':1, 'b':1} --> {'b':1} 1
            # w = {b':1,'e':1} --> {'e':1} 1
            # w = {'e':2} --> {'e':1} 1
            # s[2:3]
            
        return curr_sub_length
        
questions = [
    (
         "eceba",2,3
    ),
    (
         "aa",1,2
    ),
    (
        "abee",1,2
    ),
]

for q in questions:
    s, k, ans = q
    sol = Solution()
    for s in ['lengthOfLongestSubstringKDistinct']:
        print(getattr(sol,s)(s,k))


