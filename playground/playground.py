from itertools import combinations_with_replacement

if __name__ == '__main__':
    A, B = input().split(" ")
    [print("".join(i))  for i in combinations_with_replacement(sorted(A), int(B))]


