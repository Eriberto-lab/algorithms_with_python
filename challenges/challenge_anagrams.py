def partition(string, start, end):
    pivot_value = string[end]
    limit = start - 1

    for i in range(start, end):
        if string[i] <= pivot_value:
            limit += 1
            string[i], string[limit] = string[limit], string[i]

    string[limit + 1], string[end] = string[end], string[limit + 1]

    return limit + 1


def quick_sort(string, start, end):
    if end > start:
        part = partition(string, start, end)
        quick_sort(string, start, part - 1)
        quick_sort(string, part + 1, end)


def is_anagram(first_string, second_string):
    one = list(first_string.casefold())
    quick_sort(one, 0, len(one) - 1)

    two = list(second_string.casefold())
    quick_sort(two, 0, len(two) - 1)

    sorted_first = "".join(one)
    sorted_second = "".join(two)

    if not first_string or not second_string:
        return sorted_first, sorted_second, False
    return sorted_first, sorted_second, one == two
