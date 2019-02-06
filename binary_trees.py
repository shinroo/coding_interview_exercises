import collections


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def in_order_traversal(self, root):
        """LEFT --> ROOT --> RIGHT"""

        def in_order_traversal_helper(root):
            if root:
                in_order_traversal_helper(root.left)
                result.append(root.data)
                in_order_traversal_helper(root.right)

        result = []
        in_order_traversal_helper(root)
        return result

    def pre_order_traversal(self, root):
        """ROOT --> LEFT --> RIGHT"""

        def pre_order_traversal_helper(root):
            if root:
                result.append(root.data)
                pre_order_traversal_helper(root.left)
                pre_order_traversal_helper(root.right)

        result = []
        pre_order_traversal_helper(root)
        return result

    def post_order_traversal(self, root):
        """LEFT --> RIGHT --> ROOT"""

        def postorder_traversal_helper(root):
            if root:
                postorder_traversal_helper(root.left)
                postorder_traversal_helper(root.right)
                result.append(root.data)

        result = []
        postorder_traversal_helper(root)
        return result


def is_balanced_binary_tree(root):
    """
    Recursively call the helper function.

    """
    StatusWithHeight = collections.namedtuple("StatusWithHeight",
                                              ('balanced', 'height'))

    def is_balanced_helper(root):
        """
        Binary tree is balanced if for each node in the tree,
        the difference in the height of its left and right subtrees is
        at most 1.
        """
        # base case
        if not root:
            return StatusWithHeight(True, -1)

        # left side
        left_result = is_balanced_helper(root.left)
        if not left_result.balanced:
            return StatusWithHeight(False, 0)

        # right side
        right_result = is_balanced_helper(root.right)
        if not right_result.balanced:
            return StatusWithHeight(False, 0)

        # get height and is balanced?
        height_difference = abs(left_result.height - right_result.height)
        balanced = True
        if height_difference > 1:
            balanced = False

        height = max(left_result.height, right_result.height) + 1

        return StatusWithHeight(balanced, height)

    return is_balanced_helper(root).balanced


def is_symmetric(tree):
    """Is symmetric if the mirrored other side is the same."""

    def is_symmetric_helper(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            if (subtree_0.data == subtree_1.data
                    and is_symmetric_helper(subtree_0.left, subtree_1.right)
                    and is_symmetric_helper(subtree_0.right, subtree_1.left)):
                return True
        return False

    return not tree or is_symmetric_helper(tree.left, tree.right)


def lca(root, node1, node2):
    """
    Find the lowest common ancestor of two given nodes.

    """

    def lca_helper(root, node1, node2):
        """
        Returns: [num_target_nodes, ancestor]

        """
        if root is None:
            return [0, None]

        left_result = lca_helper(root.left, node1, node2)
        if left_result[0] == 2:
            return left_result
        right_result = lca_helper(root.right, node1, node2)
        if right_result[0] == 2:
            return right_result

        num_target_nodes = (
                left_result[0] + right_result[0] + (node1, node1).count(root)
        )

        return [num_target_nodes, root if num_target_nodes == 2 else None]

    return lca_helper(root, node1, node2)[1]


def lca_using_hash_map(node1, node2):
    """Same. Only if .parent exists in nodes."""
    iter1, iter2 = node1, node2

    seen_nodes = set()

    while iter1 and iter2:
        if iter1:
            if iter1 in seen_nodes:
                return iter1
            seen_nodes.add(iter1)
            iter1 = iter1.parent
        if iter2:
            if iter2 in seen_nodes:
                return iter2
            seen_nodes.add(iter2)
            iter2 = iter2.parent
    return None


def sum_root_to_leaf(root):
    """
        i.e. for ::    1
                    2     4

        1 -> 2 = 12
        1 -> 4 = 14
        = 26

    You basically  go and multiply the previous one with 10,
    since we are in base 10.
    Likewise with base 2 for binary.
    """

    def sum_numbers_helper(root, partial_sum):
        if not root:
            return 0

        partial_sum = partial_sum * 10 + root.data

        if not root.left and not root.right:
            return partial_sum

        return (sum_numbers_helper(root.left, partial_sum)
                + sum_numbers_helper(root.right, partial_sum))

    return sum_numbers_helper(root, 0)


def sum_root_to_leaf(tree):
    """For binary values."""

    def sum_root_to_leaf_helper(tree, partial_sum=0):
        if not tree:
            return 0

        partial_sum = partial_sum * 2 + tree.data
        if not tree.left and not tree.right:
            return partial_sum

        return (sum_root_to_leaf_helper(tree.left, partial_sum) +
                sum_root_to_leaf_helper(tree.right, partial_sum))

    return sum_root_to_leaf_helper(tree)
