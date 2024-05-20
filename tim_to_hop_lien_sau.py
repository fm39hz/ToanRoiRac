from itertools import combinations


def next_combinations(s, r, comb):
    combs = list(combinations(s, r))
    idx = combs.index(comb)
    return [combs[i] for i in range(idx + 1, idx + 26)]


if __name__ == "__main__":
    s = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    comb = ("1", "3", "6", "7", "8", "9", "A", "D", "F")
    result = next_combinations(s, 9, comb)
    print("25 tổ hợp chập 9 liền sau của tổ hợp 136789ADF:")
    for c in result:
        print("".join(c))

