import heapq


def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    sorted_arrays_iters = [iter(arr) for arr in sorted_arrays]

    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            # insert both the element and the index of the array
            heapq.heappush(min_heap, (first_element, i))

    # we can start popping + inserting from the heap
    result = []
    while min_heap:
        # we pop from the heap the current smallest value
        # and also the index of the sorted_arrays, since we inserted it before
        smallest_entry, smallest_array_idx = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_idx]
        result.append(smallest_entry)
        # now we can get the next value from the current smalles array and
        # push it to the heap, if there is one left
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_idx))
    return result


def online_median(sequence):
    """Compute running median of a sequence of numbers."""
    min_heap = []
    max_heap = []
    result = []

    for val in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, val))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        # this conditions result from Median itself.
        # if the both lists are equal that means we have to build the
        # mean of the two end values. (i.e. if len(sequence) is even)
        # if len(sequence) is odd we can just take the value of the min_heap
        if len(min_heap) == len(max_heap):
            result.append(0.5 * (min_heap[0] + -max_heap[0]))
        else:
            result.append(min_heap[0])
    return result
