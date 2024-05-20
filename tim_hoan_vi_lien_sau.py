from itertools import permutations


def next_permutations(s, n):
    perms = sorted(permutations(s))
    idx = perms.index(tuple(n))
    return [perms[i] for i in range(idx + 1, idx + 26)]


if __name__ == "__main__":
    s = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B"]
    n = ["1", "2", "8", "5", "9", "3", "4", "7", "B", "6", "A"]
    result = next_permutations(s, n)
    print("25 hoán vị liền sau của hoán vị 12859347B6A:")
    for perm in result:
        print("".join(perm))

