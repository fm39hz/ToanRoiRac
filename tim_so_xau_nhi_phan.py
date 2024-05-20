import math


def count_binary_string_with_length(length):
    return 2**length


print(f"Số xâu nhị phân độ dài 27 là: {count_binary_string_with_length(27)}")
print(
    f"Số xâu nhị phân độ dài 25 bắt đầu bằng xâu 001 là: {count_binary_string_with_length(22)}"
)


def count_binary_strings_at_least_some_bin(length):
    total_strings = 2**length
    sum_no_zeros = 1 + length + sum(math.comb(length, i) for i in range(2, 7))
    result = total_strings - sum_no_zeros
    return result


result = count_binary_strings_at_least_some_bin(31)
print(f"Số lượng xâu nhị phân độ dài 31 có chứa ít nhất 7 bit 0 là: {result}")


def binomial_coefficient(n, k):
    return math.comb(n, k)


n = 23
k = 7
result = binomial_coefficient(n, k)

print(f"Số lượng xâu nhị phân độ dài {n} và chứa đúng {k} bit 1 là: {result}")
result = binomial_coefficient(32, 11)
print(
    f"Số lượng xâu nhị phân độ dài 32 và chứa đúng 11 bit 0 và sau mỗi bit 0 là bit 1 là: {result}"
)
