"""
leetcode TopInterview 150 
226. Invert Binary Tree. Tree, Depth-First Search, Breadth-First Search, Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    stack = []
    visited = set()

    stack.append(root)
    visited.add(root)

    while stack:
        top = stack[-1]

        # 아무것도 없을때
        if not top:
            break

        # 자식 노드가 있을 경우는 타고 내려간다.
        if top.left and not top.left in visited:
            stack.append(top.left)
            visited.add(top.left)
            continue
        if top.right and not top.right in visited:
            stack.append(top.right)
            visited.add(top.right)
            continue

        # leaf에 도달했을때
        if not (top.left or top.right):
            stack.pop()
            continue

        # 반전시키기
        # 양쪽 다 있을때
        if top.left and top.right:
            top.left, top.right = top.right, top.left
            stack.pop()
            continue
        # 왼쪽만 있을때
        if top.left:
            top.left, top.right = None, top.left
            stack.pop()
            continue
        # 오른쪽만 있을때
        if top.right:
            top.left, top.right = top.right, None
            stack.pop()

    return root
