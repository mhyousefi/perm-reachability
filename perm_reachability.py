import math
from copy import deepcopy

import numpy as np

from utils import create_swap_pairs


def create_all_transformations(n, d, l):
    """

    :param n: length of each permutation
    :param d: param d specified in the assignment
    :param l: max number of permitted swap operations
    :return: a 2D list of all valid matrix transformations grouped by number of swap operations
    """

    swap_pairs = create_swap_pairs(d, n)
    res = [
        [[s] for s in swap_pairs]
    ]

    for _ in range(1, l):
        last_transformation_grp = res[-1]
        next_transformation_grp = []

        for t in last_transformation_grp:
            for p in swap_pairs:
                new_t = deepcopy(t)
                new_t.append(p)
                next_transformation_grp.append(new_t)

        res.append(next_transformation_grp)

    return res


def apply_transformation(transformation, start_perm):
    """

    :param transformation: the sequence of swap pair to apply
    :param start_perm: the permutation to start from
    :return: the resulting permutation after applying the given swap pairs
    """

    new_trans = deepcopy(start_perm)

    for swap in transformation:
        i, j = swap
        new_trans[i], new_trans[j] = new_trans[j], new_trans[i]

    return tuple(new_trans)


def create_all_reachable_permutations(n, d, l, src_perm):
    """

    :param n: length of each permutation
    :param d: param d specified in the assignment
    :param l: max number of permitted swap operations
    :param src_perm: permutation to start from
    :return: a list of all (d,l)-reachable permutations from the starting_permutation
    """

    res = set()

    transformations = create_all_transformations(n, d, l)

    for row in transformations:
        for t in row:
            res.add(apply_transformation(t, src_perm))

    return res


def is_reachable(n, d, l, start_perm, end_perm):
    """

    :param n: length of each permutation
    :param d: param d specified in the assignment
    :param l: max number of permitted swap operations
    :param start_perm: permutation to start from
    :param end_perm: permutation to reach
    :return: whether end_permutation is (d,l)-reachable from str_permutation
    """

    permutations_from_str = create_all_reachable_permutations(n, d, math.floor(l / 2), start_perm)
    permutations_from_end = create_all_reachable_permutations(n, d, math.floor(l / 2), end_perm)

    return int(permutations_from_str.intersection(permutations_from_end) != set())


if __name__ == "__main__":
    _n = 9

    str_permutation = list(range(1, _n + 1))
    end_permutation = list(range(_n, 0, -1))

    results = np.array([[None for _ in range(9)] for _ in range(4)])

    for _d in range(1, 5):
        for _l in range(1, 10):
            results[_d - 1][_l - 1] = is_reachable(_n, _d, _l, str_permutation, end_permutation)

    print(results)
