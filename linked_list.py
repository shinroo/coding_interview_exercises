class ListNode:

    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def search_list(node, key):
    while node and node.data != key:
        node = node.next
    return node


def insert_after(node, new_node):
    """basically insert in the middle of two nodes"""
    # set the next of the current node to be the next of the
    # new given node
    new_node.next = node.next
    # currently both node and new_node point at the same node
    # therefore we take nodes pointer and point it at new_node
    node.next = new_node


def delete_after(node):
    node.next = node.next.next


def merge_two_sorted_lists(list1, list2):
    dummy_head = tail = ListNode()

    while list1 and list2:

        if list1.data < list2.data:
            tail.next, list1 = list1, list1.next
        else:
            tail.next, list2 = list2, list2.next
        tail = tail.next

    # depending on which became None
    tail.next = list1 or list2
    return dummy_head.next


def reverse_linked_list(head):
    previous = None
    current = head

    while current:
        # save next node - temporary
        next_node = current.next
        # reverse pointer
        current.next = previous
        # set previous
        previous = current
        # set current
        current = next_node
        # @ also: one line swap:
        # current.next, previous, current = previous, current, current.next


def reverse_sublist(list, start, finish):
    dummy_head = sub_head = ListNode(0, list)

    for _ in range(1, start):
        sub_head = sub_head.next

    sub_iter = sub_head.next
    for _ in range(finish - start):
        sub_temp = sub_iter.next
        (sub_head.next,
         sub_iter.next,
         sub_temp.next) = (sub_temp,
                           sub_temp.next,
                           sub_head.next)
    return dummy_head.next


def has_cycle(head):
    """
    Determine if linked list has a cycle and return the
    entry node of the cycle if it has one.

    """

    def get_cycle_len(node):
        steps = 0
        runner = node
        while True:
            runner = runner.next
            steps += 1
            if runner is node:
                break
        return steps

    slow = fast = head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            new_node_1 = head
            new_node_2 = head

            # move node1 cycle len steps in
            # by doing that it is exactly cycle len steps ahead
            # and they will meet exactly at the cycle starting point!
            for _ in range(get_cycle_len(slow)):
                new_node_1 = new_node_1.next

            while new_node_1 is not new_node_2:
                new_node_1 = new_node_1.next
                new_node_2 = new_node_2.next
            return new_node_1
    return None


def overlapping_no_cycle_lists(l0, l1):
    """
    Given two linked list, both do not have cycles,
    determine if they overlap. They overlap if they point
    to one same node.
    """

    def get_list_length(node):
        length = 0
        while node:
            node = node.next
            length += 1
        return length

    len_l0 = get_list_length(l0)
    len_l1 = get_list_length(l1)

    # let l1 always be the longer list
    if len_l0 > len_l1:
        l0, l1 = l1, l0

    for _ in range(abs(len_l0 - len_l1)):
        l1 = l1.next

    while l0 and l1 and l0 is not l1:
        l0 = l0.next
        l1 = l1.next
    return l0


def overlapping_lists(l0, l1):
    """
    Given two linked list determine if they overlap.
    """
    root0 = has_cycle(l0)
    root1 = has_cycle(l1)

    # if one has a cycle the other does not --> no overlap
    if (root0 and not root1) or (not root0 and root1):
        return None
    # no cycles --> overlapping_no_cycle_lists
    elif not root0 and not root1:
        return overlapping_no_cycle_lists(l0, l1)
    # both have cycles
    else:
        temp = root1
        while temp:
            temp = temp.next
            if temp is root0 or temp is root1:
                break
    if temp is root0:
        return root1
    else:
        return None


def remove_kth_largest(llist, k):
    dummy_head = ListNode(0, llist)
    first = dummy_head.next
    second = dummy_head

    # move first node k steps in
    for _ in range(k):
        first = first.next

    # now second is exactly k steps behind the first node
    # therefore just move both forward
    # until first node is None
    while first:
        first = first.next
        second = second.next

    # finally delete kth last node
    second.next = second.next.next

    return dummy_head.next


def remove_duplicates(llist):
    iterator = llist
    while iterator:
        next_distinct = iterator
        while next_distinct and next_distinct.data == iterator.data:
            next_distinct = next_distinct.next
        iterator.next = next_distinct
        iterator = next_distinct
    return llist


def is_linked_list_a_palindrome(llist):
    slow = fast = llist

    # fast moves at twice the speed of slow
    # hence when fast is at the end
    # slow is at the middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # get first half
    first_half_it = llist
    # reverse second half of the list
    second_half_rev_it = reverse_linked_list(slow)

    while first_half_it and second_half_rev_it:
        if first_half_it.data != second_half_rev_it.data:
            return False
        first_half_it = first_half_it.next
        second_half_rev_it = second_half_rev_it.next
    return True


def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def addTwoNumbers(l1, l2):
    """
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

    """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    remain = 0
    l = ListNode()
    result = l

    while l1 is not None or l2 is not None:
        if l1 is None:
            l1 = ListNode(0)
        elif l2 is None:
            l2 = ListNode(0)
        total = l1.val + l2.val + remain
        if total >= 10:
            total = total - 10
            remain = 1
        else:
            remain = 0
        l.next = ListNode(total)
        l1 = l1.next
        l2 = l2.next
        l = l.next

    if remain == 1:
        l.next = ListNode(remain)

    return result.next
