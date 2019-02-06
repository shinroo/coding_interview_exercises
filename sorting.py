import collections


def insertion_sort(array):
    """
    O(n**2)

    """
    for i in range(1, len(array)):
        current_num = array[i]
        j = i - 1
        # Note current_num is before array[j].
        # we want to swap j such that it is less than current_num
        # and every number before current_num
        while j >= 0 and array[j] > current_num:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_num
    return array


def merge_sort(array):
    """
    O(n log n)

    """

    def merge_sort_helper(array, left, right):
        if left < right:
            middle = (left + right) // 2
            merge_sort_helper(array, left, middle)
            merge_sort_helper(array, middle + 1, right)
            array = merge(array, left, middle, right)
        return array

    def merge(array, left, middle, right):
        left_half = array[left: middle + 1]
        right_half = array[middle + 1: right + 1]
        left_half.append(float('inf'))
        right_half.append(float('inf'))
        i = j = 0
        for k in range(left, right + 1):
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
        return array

    return merge_sort_helper(array, 0, len(array) - 1)


def quicksort(array):
    """
    O(n log n)
    --> in place

    """

    def quicksort_helper(array, left, right):
        if left < right:
            pivot = partition(array, left, right)
            quicksort_helper(array, left, pivot - 1)
            quicksort_helper(array, pivot + 1, right)

    def partition(array, left, right):
        pivot_idx = get_pivot(array, left, right)
        pivot_val = array[pivot_idx]

        array[pivot_idx], array[left] = array[left], array[pivot_idx]
        border = left

        for i in range(left, right + 1):
            if array[i] < pivot_val:
                border += 1
                array[i], array[border] = array[border], array[i]
        array[left], array[border] = array[border], array[left]
        return border

    def get_pivot(array, left, right):
        middle = (left + right) // 2
        pivot = right
        if array[left] < array[middle]:
            if array[middle] < array[right]:
                pivot = middle
        elif array[left] < array[right]:
            pivot = left
        return pivot

    return quicksort_helper(array, 0, len(array) - 1)


def intersect_two_sorted_arrays(array_0, array_1):
    """
    O(m + n)

    """
    i, j, intersection = 0, 0, []

    while i < len(array_0) and j < len(array_1):
        if array_0[i] == array_1[j]:
            if i == 0 or array_0[i] != array_0[i - 1]:
                intersection.append(array_0[i])
            i += 1
            j += 1
        elif array_0[i] < array_1[j]:
            i += 1
        else:
            j += 1
    return intersection


def merge_two_sorted_arrays(array_0, len_0, array_1, len_1):
    """
    Given two sorted arrays merge them. the first given array has enough
    space in the end to fit the second array.

    """
    iter_0, iter_1, write_index = len_0 - 1, len_1 - 1, len_0 + len_1 - 1

    while iter_0 >= 0 and iter_1 >= 0:
        if array_0[iter_0] > array_1[iter_1]:
            array_0[write_index] = array_0[iter_0]
            iter_0 -= 1
        else:
            array_0[write_index] = array_1[iter_1]
            iter_1 -= 1
        write_index -= 1

    while iter_1 >= 0:
        array_0[write_index] = array_1[iter_1]
        write_index -= 1
        iter_1 -= 1


def merge(nums1, m, nums2, n):
    """
    Merge two sorted arrays where one has enough space in the end
    to store all elements combined
    i.e.
    [1,2,5, 0,0,0] , 3
    [2, 3, 4] , 3
    """
    write_index = len(nums1) - 1
    n -= 1
    m -= 1
    while n >= 0 and m >= 0:
        if nums1[m] > nums2[n]:
            nums1[write_index] = nums1[m]
            m -= 1
        else:
            nums1[write_index] = nums2[n]
            n -= 1
        write_index -= 1
    while n >= 0:
        nums1[write_index] = nums2[n]
        n -= 1
        write_index -= 1
    while m >= 0:
        nums1[write_index] = nums1[m]
        m -= 1
        write_index -= 1


def h_index(citations):
    """
    https://en.wikipedia.org/wiki/H-index

    """
    citations.sort()
    n = len(citations)
    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i
    return 0


Event = collections.namedtuple('Event', ('start', 'finish'))
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(array):
    """
    In a given list of events find the maximal amount of simultaneous occuring events.
    This can be done by getting start_time and end_time of all events and then by
    sorting the array that stores all those endpoints.
    Once sorted, iterate the endpoints list and increment num_simultaneous_events
    if endpoint is starting point
    versus decrement when event is ending point.
    + compare if if our current simultaneous event counter is the maximum value so far.

    """
    endpoints = []
    for event in array:
        endpoints.append(Endpoint(event.start, True))
        endpoints.append(Endpoint(event.finish, False))

    endpoints.sort(key=lambda e: (e.time, not e.is_start))
    max_simulataneous_events = 0
    num_simulataneous_events = 0

    for e in endpoints:
        if e.is_start:
            num_simulataneous_events += 1
            max_simulataneous_events = max(num_simulataneous_events,
                                           max_simulataneous_events)
        else:
            num_simulataneous_events -= 1
    return max_simulataneous_events


def is_array_dominated(array_0, array_1):
    """
    Given two unsorted arrays determine if the second array is dominated by the first one.
    it is dominated if all values at a specified index are smaller then the corresponding
    values at the same index of the other array.

    """
    for val_0, val_1 in zip(sorted(array_0), sorted(array_1)):
        if val_0 >= val_1:
            return False
    return True


def stable_sort_list(llist):
    def merge_two_sorted_lists(l1, l2):
        dummy_head = tail = ListNode()

        while l1 and l2:

            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy_head.next

    if llist is None or llist.next is None:
        return llist

    pre_slow, slow, fast = None, llist, llist
    while fast and fast.next:
        pre_slow = slow
        slow = slow.next
        fast = fast.next.next

    # fast reached the end of the list
    # therefore slow is exactly at the middle and
    # pre_slow is one before slow

    if pre_slow:
        # splits the lists into two equal sized lists
        # since pre_slow is one behind slow
        pre_slow.next = None

    return merge_two_sorted_lists(stable_sort_list(llist), stable_sort_list(slow))
