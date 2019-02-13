import math

from utils import *


def create_trans_matrix(swap_pair, n):
    """

    :param swap_pair: containing two indices, which indicate which two items in the permutation will be swapped
    :param n: length of each permutation
    :return: the corresponding matrix representation for the given swap pair
    """

    i, j = swap_pair
    temp = np.eye(n)

    temp[i][i] = 0
    temp[j][j] = 0

    temp[i][j] = 1
    temp[j][i] = 1

    return temp


def create_pd_matrices(n, d):
    """

    :param n: length of each permutation
    :param d: parameter restricting the distance of swap pair elements
    :return: a list of matrix representations corresponding to all valid transformations with one swap operation
    """

    res = []

    for s in create_swap_pairs(d, n):
        res.append(create_trans_matrix(swap_pair=s, n=n))

    return res


def create_permutations_with_one_more_swap(pd_matrices, cur_permutations):
    """

    :param pd_matrices: list of matrix representations for all valid swap pairs
    :param cur_permutations: permutations created up to now
    :return: all valid transformations with one more swap operation
    """

    res = []

    for p_vector in cur_permutations:
        for swap_matrix in pd_matrices:
            res.append(np.matmul(swap_matrix, p_vector))

    return res


def add_new_permutations(cur_permutations, pd_matrices):
    """

    :param cur_permutations: a list of current permutations
    :param pd_matrices: list of matrix representations for all valid swap pairs
    :return:
    """

    new_permutations = create_permutations_with_one_more_swap(pd_matrices, cur_permutations=cur_permutations)

    for p in new_permutations:
        cur_permutations.append(p)

    return remove_duplicates(np_arrays=cur_permutations)


def create_all_reachable_permutations(n, d, l, str_permutation, end_permutation):
    """

    :param n: length of each permutation
    :param d: parameter restricting the distance of swap pair elements
    :param l: max number of permitted swap operations
    :param str_permutation: permutation to start from
    :param end_permutation: permutation to arrive at
    :return: two lists each containing all (d,l)-reachable permutations from str_permutation and end_permutation respectively
    """

    pd_matrices = create_pd_matrices(n, d)

    permutations_from_str = [np.matmul(str_permutation, x) for x in pd_matrices]
    permutations_from_end = [np.matmul(end_permutation, x) for x in pd_matrices]

    for _ in range(1, l):
        permutations_from_str = add_new_permutations(cur_permutations=permutations_from_str, pd_matrices=pd_matrices)
        permutations_from_end = add_new_permutations(cur_permutations=permutations_from_end, pd_matrices=pd_matrices)

    return permutations_from_str, permutations_from_end


def is_reachable(n, d, l, str_permutation, end_permutation):
    """

    :param n: length of each permutation
    :param d: parameter restricting the distance of swap pair elements
    :param l: max number of permitted swap operations
    :param str_permutation: permutation to start from
    :param end_permutation: permutation to reach
    :return: whether end_permutation is (d,l)-reachable from str_permutation
    """

    permutations_from_str, permutations_from_end = create_all_reachable_permutations(
        n, d, math.floor(l / 2), str_permutation, end_permutation
    )

    return have_intersection(permutations_from_str, permutations_from_end)


if __name__ == "__main__":
    _n = 9

    str_permutation = list(range(1, _n + 1))
    end_permutation = list(range(_n, 0, -1))

    results = np.array([[None for _ in range(9)] for _ in range(4)])

    for _d in range(1, 5):
        for _l in range(1, 10):
            results[_d - 1][_l - 1] = int(is_reachable(_n, _d, _l, str_permutation, end_permutation))

    print(results)
