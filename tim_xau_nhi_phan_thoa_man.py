import math


def count_strings(n, k):
    return math.comb(n, k)


def total_count_strings():
    return count_strings(19, 11) + count_strings(20, 10)


result = total_count_strings()
print(f"Số lượng xâu độ dài 30 thỏa mãn ít nhất một trong hai điều kiện là: {result}")
