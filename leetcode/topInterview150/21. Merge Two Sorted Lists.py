"""
leetcode Top Interview 150 21. Merge Two Sorted Lists. Linked List, Recursion

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    head: Optional[ListNode] = ListNode()
    current = head

    while list1 and list2:
        if list1.val <= list2.val:  # list1이 작거나 같을 경우
            # 먼저 current next에 list1을 넣어주고
            current.next = list1
            list1 = list1.next  # list1 다음 노드로 이동하고
            current = current.next  # current도 다음 노드로 이동

        else:  # list2가 작을경우
            current.next = list2
            list2 = list2.next
            current = current.next

    if list1:
        current.next = list1
    if list2:
        current.next = list2

    return head.next


mergeTwoLists([1, 2, 4], [1, 3, 4])