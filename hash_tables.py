import collections


def is_anagram(str1, str2):
    """
    A string is an anagram of another string, if we can rearrange its
    letters and get the other string.
    Hence the strings must be of same length and contain the same
    number of each letter.

    """
    if len(str1) != len(str2):
        return False

    chars = dict()

    for ch in str1:
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 0

    for ch in str2:
        if ch not in chars or chars[ch] < 0:
            return False
        else:
            chars[ch] -= 1
    return True


def can_form_palindrome(s):
    """
    A string can form a palindrome if the count for all letters is even
    for all letters or if the count for all letters is even except
    for one letter, for which the count is odd.
    """
    n_odd = 0
    for count in collections.Counter(s).values():
        if count % 2 == 1:
            n_odd += 1
    return n_odd <= 1


def can_form_palindrome_slower(string):
    char_count = dict()
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    n_odd = 0
    for count in char_count.values():
        if count % 2 == 1:
            n_odd += 1
    return n_odd <= 1


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    """len(magazine_text) >= len(letter_text)"""
    char_freq_letter = collections.Counter(letter_text)

    for char in magazine_text:
        if char in char_freq_letter:
            char_freq_letter[char] -= 1
            if char_freq_letter[char] == 0:
                del char_freq_letter[char]
                # if there are not counts left in the table
                # we can return true already
                if not char_freq_letter:
                    return True
    return not char_freq_letter


def lca(node0, node1):
    """Only works if .parent exists."""
    iter0, iter1 = node0, node1
    nodes_on_path_set = set()

    while iter0 or iter1:

        if iter0:
            if iter0 in nodes_on_path_set:
                # in this case iter1 has already
                # appended our current to set and we
                # found ancestor
                return iter0
            nodes_on_path_set.add(iter0)
            iter0 = iter0.parent
        if iter1:
            if iter1 in nodes_on_path_set:
                # iter0 has added. we found ancestor
                return iter1
            nodes_on_path_set.add(iter1)
            iter1 = iter1.parent
    return None


def longest_subarray_with_distinct_entries(array):
    most_recent_occurences = dict()
    longest_dub_free_subarray_start_idx = result = 0

    for i, val in enumerate(array):
        if val in most_recent_occurences:
            dup_idx = most_recent_occurences.get(val)
            # if the value accured before we started our current subarray
            # we do not care about the duplicate
            # otherwise (i.e. here) we either get a new longest subarray or not
            if dup_idx >= longest_dub_free_subarray_start_idx:
                result = max(result, i - longest_dub_free_subarray_start_idx)
                # this is now our new longest sequence with the
                # start inded shifted one after the original occurence of
                # our current duplicate
                longest_dub_free_subarray_start_idx = dup_idx + 1
        else:
            most_recent_occurences[val] = i
    return max(result, len(array) - longest_dub_free_subarray_start_idx)
