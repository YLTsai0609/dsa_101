"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

easy

no extra space for another array, modifiying the input array in-place

nums = [1,1,2]
out : 2, nums = [1,2, _]

nums = [0,0,1,1,1,2,2,3,3,4]
out : 5, nums = [0,1,2,3,4,_,_,_,_,_]

nums 的長度限制在 1, 3 * 10^4 之間
-100 <- num[i] <= 100
"""

"""
idea 1 : 因為是排序好的，所以重複值必定在 index 上會相臨，可以用雙指針，一次指向兩個來比較，並且用一個 counter 維護目前有幾個獨立值
"""


from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linkedlist(arr: List[int]) -> ListNode:
    for i, e in enumerate(reversed(arr)):
        if i == 0:
            node = ListNode(val=e)
            tail = node
        else:
            node = ListNode(val=e, next=tail)
            tail = node
    return node


def display_linkedlist(head: ListNode) -> None:
    while head:
        print(head.val)
        head = head.next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        tc : O(N)
        sc : O(1)
        """
        if not head:
            return None
        slow = head
        fast = head

        while fast:
            if slow.val != fast.val:
                # find unique
                slow.next = fast
                slow = fast

            # find duplicates, keep traverse
            fast = fast.next

        return head


if __name__ == "__main__":
    nums1 = [1, 1, 2]
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # nums2 = [
    #     1,
    #     1,
    #     2,
    #     3,
    #     3,
    # ] # buggy

    n = create_linkedlist(nums2)
    display_linkedlist(n)
    print("Solving....")
    sol = Solution().deleteDuplicates(n)
    display_linkedlist(sol)
