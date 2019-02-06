def is_palindromic(string):
    for i in range(len(string) // 2):
        if not string[i] == string[~i]:
            return False
    return True


def replace_and_remove(size, s):
    """
    Replace each 'a' by two 'd's and
    delete each entry containing a 'b'.
    """
    # forward pass
    write_idx = 0
    a_count = 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1

    # backward pass
    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx - 1: write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return final_size


def is_palindrome(s):
    """
    String is palindromic if it reads the same backwards,
    skipping non alphanumeric characters and ignoring cases.
    """
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True


def reverse_from_to(s, start, finish):
    while start < finish:
        s[start], s[finish] = s[finish], s[start]
        start += 1
        finish -= 1


def reverse_words(s):
    """
    Reverse a string containing words which are separated by
    whitespace get all words in reverse order.

    my name is ---> is my name

    """
    s.reverse()

    start = 0
    while True:
        finish = s.find(b' ', start)
        # .find() returns -1 if nothing found
        if finish < 0:
            break
        reverse_from_to(s, start, finish - 1)
        start = finish + 1
    # reverse the last word
    reverse_from_to(s, start, len(s) - 1)


def encoding(s):
    """
    'aaabbcccd' --> '3a2b3c1d'

    """
    result = []
    count = 1
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i - 1]:
            result.append(str(count) + s[i - 1])
            count = 1
        else:
            count += 1

    return "".join(result)


def decoding(s):
    """
    '3a2b3c1d' --> 'aaabbcccd'

    """
    count = 0
    result = []
    for c in s:
        if c.isdigit():
            count = count * 10 + int(c)
        else:
            if count == 0:
                count = 1
            result.append(c * count)
            count = 0
    return ''.join(result)


if __name__ == "__main__":
    print(is_palindromic('hannah'))
    print(is_palindromic('annah'))
