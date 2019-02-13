import numpy as np


def create_swap_pairs(d, n):
    """

    :param d: restricts the distance of swap pair elements: d <= j - i <= n - d
    :param n: length of each permutation
    :return: all valid index pairs for which a swap can take place
    """

    res = [(0, 0)]

    for i in range(n):
        for j in range(i + 1, n):
            if i == j or d <= j - i <= n - d:
                res.append((i, j))

    return res


def have_intersection(l1, l2):
    t1 = set((a.tostring(), a.dtype) for a in l1)
    t2 = set((a.tostring(), a.dtype) for a in l2)

    return t1.intersection(t2) != set()


def remove_duplicates(np_arrays):
    """

    :param np_arrays: list of numpy array objects
    :return: returns the same list after removing duplicate elements
    """

    temp = set((a.tostring(), a.dtype) for a in np_arrays)
    return [np.fromstring(a, dtype=dtype) for a, dtype in temp]
