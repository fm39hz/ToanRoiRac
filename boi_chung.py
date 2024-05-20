def find_numbers_divisible(start, end, divisor):
    result = []
    for num in range(start, end + 1):
        if num % divisor == 0:
            result.append(num)
    write_result(str(divisor), str(result))


def find_numbers_same_divisible(start, end, divisors):
    result = set()

    for num in range(start, end + 1):
        is_common_multiple = all(num % divisor == 0 for divisor in divisors)
        if is_common_multiple:
            result.add(num)

    write_result("_".join(str(divisor) for divisor in divisors), str(result))


def write_result(number, results):
    for result in results:
        with open(f"{number}_result.txt", "w") as f:
            f.write(result)


start = 22218782
end = 67220244
divisors = [297, 3969, 41503]

for divisor in divisors:
    find_numbers_divisible(start, end, divisor)
    find_numbers_same_divisible(start, end, [divisors[0], divisors[1]])
    find_numbers_same_divisible(start, end, [divisors[1], divisors[2]])
    find_numbers_same_divisible(start, end, [divisors[0], divisors[2]])
    find_numbers_same_divisible(start, end, divisors)
