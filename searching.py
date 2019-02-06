import bisect
import collections


def binary_search(val, array):
    """
    Classic binary search. O(log n)

    """
    lower, upper = 0, len(array) - 1

    while lower <= upper:
        middle = lower + (upper - lower) // 2
        if array[middle] == val:
            return middle
        elif array[middle] < val:
            lower = middle + 1
        else:
            upper = middle - 1
    return - 1


def search(val, array):
    """Recursive version. O(log n)"""

    def bin_search_helper(lower, upper):
        if lower <= upper:
            middle = lower + (upper - lower) // 2
            if array[middle] == val:
                return middle
            elif array[middle] < val:
                return bin_search_helper(middle + 1, upper)
            else:
                return bin_search_helper(lower, middle - 1)

    lower, upper = 0, len(array) - 1
    res = bin_search_helper(lower, upper)
    return -1 if res is None else res


def search_first_of_k(array, k):
    """
    Search first appearance of k
    e.g. [1, 2, 3, 3, 3, 3, 5, 5, 8], k = 3
    then we want to get back index = 2
    and not index = 4 or 5
    because we want first occurence
    this is basically binary search which
    repeated binary search if the element was found.

    """
    lower, upper = 0, len(array) - 1
    result = -1

    while lower <= upper:
        middle = lower + (upper - lower) // 2
        if array[middle] == k:
            result = middle
            upper = middle - 1

        elif array[middle] > k:
            upper = middle - 1

        else:
            lower = middle + 1
    return result


def search_entry_equal_to_its_index(array):
    """
    e.g. [4, 4, 4, 5, 5, 6, 6]
    here we would return index 6 since it
    is the first value where index == value

    """
    lower, upper = 0, len(array) - 1

    while lower <= upper:
        middle = lower + (upper - lower) // 2
        difference = array[middle] - middle
        if difference == 0:
            return middle
        elif difference > 0:
            upper = middle - 1
        else:
            lower = middle + 1
    return -1


def search_smallest(array):
    """
    Cyclically sorted array. [3, 4, 5, 1, 2, 3]

    """
    lower, upper = 0, len(array) - 1
    while lower < upper:
        middle = lower + (upper - lower) // 2

        if array[middle] > array[upper]:
            lower = middle - 1
        else:
            right = middle
    return lower


def square_root(k):
    """
    Find the largest integer whose square is less than or equal to k.

    """
    lower, upper = 0, k

    while lower <= upper:
        middle = lower + (upper - lower) // 2
        middle_squared = middle * middle
        # if it is actually lower than increase it and see if we can go bigger
        if middle_squared <= k:
            lower = middle + 1
        # otherwise we have to decrease anyways
        else:
            upper = middle - 1
    return lower - 1


def matrix_search(matrix, x):
    """
    Search for x in given matrix.
    All values in rows of matrix are sorted.
    All value in columns of matrix are sorted.
    i.e. all values in a given row to the left of a value
    are bigger than itself.
    likewise all values in the given column below the value
    are greater than itself.
    """
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == x:
            return True
        # eliminates row since last value in the row is smaller than x
        # hence the x cannot be in the row
        elif matrix[row][col] < x:
            row += 1
        # the value in the current row in the current column
        # is greater than x. hence we know that the value could be in this
        # row and furthermore we know that the value cannot be in the current column
        # since all the values in this column are greater than the current one
        else:
            col -= 1
    return False


def find_kth_largest(k, array):
    heap = []
    import heapq
    for num in array:
        heapq.heappush(heap, -num)

    for _ in range(k):
        res = heapq.heappop(heap)
    return -res


Student = collections.namedtuple('Student', ('name', 'grade_point_average'))


def search_student(students, target):
    def compare_gpa(student):
        return (-student.grade_point_average, student.name)

    i = bisect.bisect_left([compare_gpa(s) for s in students], compare_gpa(target))

    return 0 <= i < len(students) and students[i] == target
