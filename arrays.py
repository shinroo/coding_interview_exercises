import random
import math
import copy


def even_odd(array):
    next_even = 0
    next_odd = len(array) - 1

    while next_even < next_odd:
        if array[next_even] % 2 == 0:
            next_even += 1
        else:
            array[next_even], array[next_odd] = array[next_odd], array[next_even]
            next_odd -= 1


def dutch_flag_partition(pivot_index, array):
    pivot = array[pivot_index]

    smaller = 0
    larger = len(array)
    equal = 0

    while equal < larger:
        if array[equal] < pivot:
            array[smaller], array[equal] = array[equal], array[smaller]
            smaller += 1
            equal += 1
        elif array[equal] > pivot:
            larger -= 1
            array[equal], array[larger] = array[larger], array[equal]
        else:
            equal += 1


def generate_primes_naive(n):
    """
    Given n, return all primes up to and including n.

    """

    def is_prime(n):
        if abs(n) <= 2:
            return True

        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True

    primes = []

    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def generate_primes_better(n):
    """
    Given n, return all primes up to and including n.

    """
    primes = []

    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            # starting from 2 time the prime number going up to n in p steps.
            for i in range(p * 2, n + 1, p):
                is_prime[i] = False
    return primes


def random_sampling(n, array):
    for i in range(n):
        random_index = random.randint(i, len(array) - 1)
        array[i], array[random_index] = array[random_index], array[i]


def compute_random_permutation(n):
    array = list(range(n))
    random_sampling(n, array)
    return array


def is_valid_sudoku(partial_assignment):
    """
    Sodoku is valid if in each row, each column
    and each subsquare with length math.sqrt(len(partial_assignment))
    contains the numbers 0 to len(partial_assignment) - 1.

    """

    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n_rows = len(partial_assignment)
    n_cols = len(partial_assignment[0])

    for i in range(n_rows):
        if has_duplicate(partial_assignment[i]):
            return False
        elif has_duplicate([partial_assignment[j][i] for j in range(n_cols)]):
            return False

    square_size = int(math.sqrt(n_rows))

    # checks the individual squares
    for i in range(square_size):
        for j in range(square_size):
            if has_duplicate([
                partial_assignment[a][b]
                for a in range(square_size * i, square_size * (i + 1))
                for b in range(square_size * j, square_size * (j + 1))]):
                return False
    return True


def rotate_matrix(square_matrix):
    """Rotate a given n x n matrix by 90 degreees clockwise inplace."""
    dim = len(square_matrix) - 1
    for i in range(len(square_matrix) // 2):
        for j in range(i, dim - i):
            # for first iteration:
            # square_matrix[i][j] --> left upper corner
            # square_matrix[j][~i] --> right upper corner
            # square_matrix[~i][~j] --> right lower corner
            # square_matrix[~j][i] --> left lower corner
            (square_matrix[i][j],
             square_matrix[j][~i],
             square_matrix[~i][~j],
             square_matrix[~j][i]) = (square_matrix[~j][i],
                                      square_matrix[i][j],
                                      square_matrix[j][~i],
                                      square_matrix[~i][~j])


def generate_pascal_triangle(n):
    result = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result


def merge(nums1, m, nums2, n):
    """
    Merge two sorted arrays where one has enough space in the end
    to store all elements of both.
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


def transpose_matrix(matrix):
    result = []
    for i in range(len(matrix[0])):
        result.append([matrix[j][i] for j in range(len(matrix))])
    return result


def transpose(matrix):
    """in place"""
    for i in range(len(matrix[0])):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def two_sum(nums, target):
    """
    Given an array of numbers check if some pair of numbers
    adds up to target.
    """
    nums_dict = dict()
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_dict:
            return [i, nums_dict[complement]]
        else:
            nums_dict[num] = i


def remove_duplicates(nums):
    """Given a sorted array remove all the duplicates in place."""
    if not nums:
        return 0

    write_index = 1
    for i in range(1, len(nums)):
        if nums[write_index - 1] != nums[i]:
            nums[write_index] = nums[i]
            write_index += 1
    return write_index


def permute(nums):
    """
    Given a collection of distinct integers,
    return all possible permutations.

    """

    def directed_permutations(i):
        if i == len(nums) - 1:
            result.append(copy.copy(nums))
            return
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            directed_permutations(i + 1)
            nums[i], nums[j] = nums[j], nums[i]

    result = []
    directed_permutations(0)
    return result
