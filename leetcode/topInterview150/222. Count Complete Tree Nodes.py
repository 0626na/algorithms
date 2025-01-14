"""
leetcode TopInterview 150
222. Count Complete Tree Nodes 

Binary Search, Bit Manipulation, Tree, Binary Tree

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compute_depth(node: TreeNode) -> int:
    """
    트리의 왼쪽 자식을 따라가면서
    '루트 레벨로부터 몇 번 내려갈 수 있는가'를 센다.
    예) 아래 트리라면,
         1
        / \
       2   3
      /
     4
    왼쪽으로 2번 더 내려갈 수 있으므로 depth=2
    """
    depth = 0
    while node.left:
        node = node.left
        depth += 1
    return depth


def exists(index: int, depth: int, node: TreeNode) -> bool:
    """
    마지막 레벨(깊이=depth)에 0-based 인덱스 'index' 위치의 노드가
    실제로 존재하는지 True/False로 알려주는 함수.

    left, right = 0, 2**depth - 1 로 초기화한 뒤
    이진탐색 아이디어로 'index'가 왼쪽 범위인지 오른쪽 범위인지 따라
    node=node.left / node=node.right 로 이동하며 확인.
    중간에 node가 None이 되면 해당 index에는 노드가 없는 것(False).
    """
    left, right = 0, 2**depth - 1
    for _ in range(depth):
        mid = (left + right) // 2
        if index <= mid:
            node = node.left
            right = mid
        else:
            node = node.right
            left = mid + 1
        if not node:
            return False
    return True


def countNodes(root: Optional[TreeNode]) -> int:
    """
    완전 이진 트리 노드 수를 구하는 최종 함수.
    1) compute_depth로 깊이(마지막 레벨 전까지 몇 번 내려가는지)를 구하고
    2) 마지막 레벨의 인덱스 범위(0 ~ 2^depth - 1)에 대해,
       exists(mid, depth, root)로 실제 노드 존재 여부를 이진탐색 방식으로 확인.
    3) '존재'하는 노드가 몇 개인지 찾아서, '2^depth - 1 + 그 개수' 합을 리턴.
    """
    if not root:
        return 0

    depth = compute_depth(root)
    if depth == 0:
        return 1  # 루트밖에 없는 트리

    # 마지막 레벨에서 가능한 인덱스 범위: 0 ~ (2^depth - 1)
    left, right = 0, 2**depth - 1
    while left <= right:
        mid = (left + right) // 2
        # mid 위치의 노드가 있으면 left=mid+1, 없으면 right=mid-1
        if exists(mid, depth, root):
            left = mid + 1
        else:
            right = mid - 1

    # depth 레벨 전까지 노드 수 = 2^depth - 1
    # 마지막 레벨에서 존재하는 노드 수 = left
    return (2**depth - 1) + left
