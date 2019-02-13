def create_swap_pairs(d, n):
    """

    :param d: param d specified in the assignment
    :param n: length of each permutation
    :return: all valid index pairs for which a swap can take place
    """

    res = [(0, 0)]

    for i in range(n):
        for j in range(i + 1, n):
            if i == j or d <= j - i <= n - d:
                res.append((i, j))

    return res
