'''
sorted array

nums = [-7, -4, 0, 2, 5, 10]

use double index to get squared sorted result 
'''

from typing import List

def sol(nums : List[int]) -> List[int]:
    '''
    double index, 頭跟尾比，尾會是最大的，頭可能平方後會比尾巴大，就必須插在對應位置，同時尾要退後一格

    round 1
        i = 0, j = 5
        -7 --> 49
        10 --> 100
        100 比較大，100放原本的位置
        [None, None, ..., 100]
        j -= 1

    round 2
        i = 0, j = 4
        49
        5 --> 25
        49 比較大，49 放在 j 的位置
        i += 1
        j -= 1

    [None, None, ... , 49, 100]

    round 3
        i = 1, j = 3
        -4 --> 16
        25
        25 比較大，25 放在 j 的位置
        j -= 1

        [None, None, 25 , 49, 100]

    round 4
        i = 1, j = 2
        16
        2 --> 4
        16 比較大，16 放在 j 的位置

        [None, ...,16, 25 , 49, 100]

        i += 1
        j-= 1


    round 5
        i = 2
        j = 1
        4 
        0
        4比較大，4放在 j 的位置
        j -= 1

    round 6
        j = 0
        i = 2
        將 i = 2 的元素直接放在 0 結束
    

    '''

    res = [None for _ in range(len(nums))]
