from itertools import combinations_with_replacement
from itertools import product, permutations, combinations


def iter_product():
    """
    (1,2) X (4,5) => (1,4) (1,5) (2,4) (2,5)
    """
    A = [int(i) for i in input().split(" ")]
    B = [int(i) for i in input().split(" ")]

    print(list(product(A, B)))


def iter_permutations():
    """
    HACK 2 => AC /n AH/n AK/n ...
    """
    A, B = input().split(" ")
    C = int(B)
    [print("".join(i)) for i in permutations(sorted(A), C)]


def iter_combinations():
    """
    print list(combinations('12345',2))
    [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ...
    """
    A, B = input().split(" ")
    sorted_A = sorted(A)
    [print("".join(i)) for index in range(1, int(B) + 1, 1) for i in combinations(sorted_A, index)]


def iter_combinations_replace():
    """
    list(combinations_with_replacement('12345',2))
    [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3')
    """
    A, B = input().split(" ")
    [print("".join(i)) for i in combinations_with_replacement(sorted(A), int(B))]
