"""
leetcode TopInterview 150 100. Same Tree. Tree, Depth-First Search, Breadth-First Search, Binary Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    stack_p = []
    stack_q = []
    visited_p = set()
    visited_q = set()

    stack_p.append(p)
    stack_q.append(q)

    visited_p.add(p)
    visited_q.add(q)

    while stack_p and stack_q:
        p_node = stack_p[-1]
        q_node = stack_q[-1]

        if not p_node and not q_node:
            return True
        if not p_node:
            return False
        if not q_node:
            return False

        if p_node.val != q_node.val:
            return False
        if (p_node.left and not q_node.left) or (not p_node.left and q_node.left):
            return False
        if (p_node.right and not q_node.right) or (not p_node.right and q_node.right):
            return False

        if (p_node.left and q_node.left) and p_node.left.val != q_node.left.val:
            return False
        if (p_node.right and q_node.right) and p_node.right.val != q_node.right.val:
            return False

        if not p_node.left in visited_p and p_node.left:
            stack_p.append(p_node.left)
            visited_p.add(p_node.left)
        elif not p_node.right in visited_p and p_node.right:
            stack_p.append(p_node.right)
            visited_p.add(p_node.right)
        else:
            stack_p.pop()

        if not q_node.left in visited_q and q_node.left:
            stack_q.append(q_node.left)
            visited_q.add(q_node.left)
        elif not q_node.right in visited_q and q_node.right:
            stack_q.append(q_node.right)
            visited_q.add(q_node.right)
        else:
            stack_q.pop()

    return True


isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)))
