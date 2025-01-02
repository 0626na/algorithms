"""
leetcode Top Interview150 104. Maximum Depth of Binary Tree. Tree, Depth-First Search, Breadth-First Search, Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""

from typing import List, Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    stack: List[Tuple[TreeNode, int]] = []
    visited = set()
    level = 1

    if not root:
        return 0

    stack.append((root, 1))
    visited.add(root)

    while stack:
        node, depth = stack[-1]

        if node.left and not node.left in visited:
            stack.append((node.left, depth + 1))
            visited.add(node.left)

        elif node.right and not node.right in visited:
            stack.append((node.right, depth + 1))
            visited.add(node.right)

        else:
            node, depth = stack.pop()
            if level < depth:
                level = depth

    return level


# maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))

maxDepth(
    TreeNode(
        0,  # val
        TreeNode(0, TreeNode(0, None, None), None),  # left  # left  # right
        TreeNode(0, None, TreeNode(0, None, TreeNode(0, None, None))),  # right
    )
)
