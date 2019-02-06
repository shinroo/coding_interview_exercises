class BstNode:

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def search_bst(tree, key):
    """
    takes advantage of the property of BST, that
    the key stored at a node is grater than or equal to the keys stored
    at the nodes of its left subtree and less than or equal to the keys stored
    in the nodes of its right subtree.

    """
    if not tree or tree.data == key:
        return tree
    elif key < tree.data:
        return search_bst(tree.left, key)
    else:
        return search_bst(tree.right, key)


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    """
    O(n)

    """
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    else:
        return (is_binary_tree_bst(tree.left, low_range, tree.data)
                and
                is_binary_tree_bst(tree.right, tree.data, high_range))


def is_binary_tree_bst_alternative(tree):
    def in_order_traversal(tree):
        if not tree:
            return True
        elif not in_order_traversal(tree.left):
            return False
        elif prev[0] and prev[0].data < tree.data:
            return False
        prev[0] = tree
        return in_order_traversal(tree.right)

    prev = [None]
    return in_order_traversal(tree)


def find_first_greater_than_k(tree, k):
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far = subtree
            subtree = subtree.left
        else:
            subtree = subtree.right
    return first_so_far


def find_k_largest_in_bst(tree, k):
    def find_k_largest_in_bst_helper(tree):
        if tree and len(k_largest_elements) < k:
            find_k_largest_in_bst_helper(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)

    k_largest_elements = []
    find_k_largest_in_bst_helper(tree)
    return k_largest_elements


def find_LCA(tree, s, b):
    """
    Input nodes are nonempty and the key at s is less than or equal to that of b.

    """
    while tree.data < s.data or tree.data > b.data:
        while tree.data < s.data:
            tree = tree.right
        while tree.data > b.data:
            tree = tree.left
    return tree


def find_lca_in_bst(tree, s, b):
    while tree.data < s.data or tree.data > b.data:
        while tree.data < s.data:
            tree = tree.right
        while tree.data > b.data:
            tree = tree.left
    return tree


def build_min_height_bst_from_sorted_array(array):
    """
    Given a sorted array build the binary search tree representation of it.
    Since the array is sorted we can take its middle element, which will be
    the root of the BST. we can just do this recursively for the right
    and left part of the array.

    """

    def build_min_height_bst_from_sorted_subarray(start, end):
        if start >= end:
            return None
        middle = (start + end) // 2
        return BstNode(array[middle],
                       build_min_height_bst_from_sorted_subarray(start, middle),
                       build_min_height_bst_from_sorted_subarray(middle + 1, end))

    return build_min_height_bst_from_sorted_subarray(0, len(array))
