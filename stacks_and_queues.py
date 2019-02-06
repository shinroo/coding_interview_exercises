def print_linked_list_in_reverse(llist):
    nodes = []
    while llist:
        nodes.append(llist.data)
        llist = llist.next
    while nodes:
        print(nodes.pop())


def is_well_formed(s):
    """
    Determine if given string of ( ) [ ] { } is well formed.
    It is well formed if a given paranthesis is closed with the
    corresponding counterpart.

    """
    left_chars = []
    lookup_table = {"(": ")", "[": "]", "{": "}"}

    for c in s:
        # if it is a opening parenth append it to the stack
        if c in lookup_table:
            left_chars.append(c)
        # if it is no opening parenth we want to check if
        # the last parenth was the corresponding counterpart
        elif not left_chars or lookup_table[left_chars.pop()] != c:
            return False

    return not left_chars


def shortest_equivalent_path(path):
    if not path:
        raise ValueError("Empty string is not valid")

    path_names = []

    if path[0] == "/":
        path_names.append('/')

    for token in (token for token in path.split('/')
                  if token not in ['.', '']):
        if token == '..':
            if not path_names or path_names[-1] == '..':
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise ValueError("path error")
                path_names.pop()
        else:
            path_names.append(token)
    result = '/'.join(path_names)
    if result.startswith('//'):
        result = result[1:]
    return result


def binary_tree_depth_order(tree):
    result = []
    if not tree:
        return result
    curr_depth_nodes = [tree]

    while curr_depth_nodes:
        # append the current top most level to nodes to the result
        result.append([curr.data for curr in curr_depth_nodes])

        # get the next highest level nodes of the tree
        # i.e. all the childs of the current nodes.
        curr_depth_nodes = [
            child for curr in curr_depth_nodes
            for child in (curr.left, curr.right)
            if child
        ]
    return result


# Implement queue using stacks
class MyQueue(object):

    def __init__(self):
        self.enq = []
        self.deq = []

    def push(self, x):
        self.enq.append(x)

    def pop(self):
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
        return self.deq.pop()

    def peek(self):
        return self.enq[0] if not self.deq else self.deq[-1]

    def empty(self):
        return not self.enq and not self.deq
