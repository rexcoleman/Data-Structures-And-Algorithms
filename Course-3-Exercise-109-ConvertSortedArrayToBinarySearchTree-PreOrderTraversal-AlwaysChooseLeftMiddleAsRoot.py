from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            # Always choose left middle as root
            p = (left + right) // 2
            # Preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        return helper(0, len(nums) - 1)




def bstToList(root: Optional[TreeNode]) -> List[int]:

    result = []
    if not root:
        return result
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result






if __name__ == '__main__':

    # Inputs
    nums1 = [-10, -3, 0, 5, 9]
    nums2 = [1, 3]

    # Construct binary search trees
    binary_search_tree_1 = Solution()
    binary_search_tree_2 = Solution()

    bst_1 = binary_search_tree_1.sortedArrayToBST(nums1)
    bst_2 = binary_search_tree_2.sortedArrayToBST(nums2)

    # Convert BSTs back to lists
    list_1 = bstToList(bst_1)
    list_2 = bstToList(bst_2)

    print(f"Output 1: {list_1}")
    print(f"Output 2: {list_2}")

