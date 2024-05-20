start = 22218782
end = 67220244
nums = [297, 3969, 41503]

print_divisors = ",".join(str(num) for num in nums)


def is_true(i, divisor):
    return i % divisor == 0


def count_divisor():
    counter_a = 0
    counter_b = 0
    counter_c = 0
    for i in range(start, end):
        if is_true(i, nums[0]) and is_true(i, nums[1]) and is_true(i, nums[2]):
            counter_a += 1
        elif is_true(i, nums[0]) or is_true(i, nums[1]):
            counter_b += 1
        elif is_true(i, nums[0]) or is_true(i, nums[1]) or is_true(i, nums[2]):
            counter_c += 1
    print(f" Số các số chia hết cho cả {print_divisors} là: {counter_a}")
    print(f" Số các số chia hết cho hoặc {nums[0]} hoặc {nums[1]} là: {counter_b}")
    print(f" Số các số chia hết cho ít nhất một trong {print_divisors} là: {counter_c}")


count_divisor()
