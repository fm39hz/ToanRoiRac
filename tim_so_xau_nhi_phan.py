import math


def binomial_coefficient(n, k):
    return math.comb(n, k)


n = 23
k = 7
result = binomial_coefficient(n, k)

print(f"Số lượng xâu nhị phân độ dài {n} và chứa đúng {k} bit 1 là: {result}")
