start = 22218782
end = 67220244
nums = [297, 3969, 41503]

print_divisors = ",".join(str(num) for num in nums)


def chiahet(i, divisor):
    return i % divisor == 0


def count_divisor():
    counter_a = 0
    counter_b = 0
    counter_c = 0
    counter_d = 0
    counter_e = 0
    counter_f = 0
    counter_g = 0
    counter_h = 0
    for i in range(start, end):
        if chiahet(i, nums[0]) and chiahet(i, nums[1]) and chiahet(i, nums[2]):
            counter_a += 1
        if chiahet(i, nums[0]) or chiahet(i, nums[1]):
            counter_b += 1
        if chiahet(i, nums[0]) and not chiahet(i, nums[2]):
            counter_c += 1
        if chiahet(i, nums[0]) or chiahet(i, nums[1]) or chiahet(i, nums[2]):
            counter_d += 1
        if chiahet(i, nums[1]) and chiahet(i, nums[2]) and not chiahet(i, nums[0]):
            counter_f += 1
        for divisor in nums:
            if i % divisor == 0:
                counter_g += 1
                break
        divisors = [divisor for divisor in nums if i % divisor == 0]
        if len(divisors) == 2:
            counter_h += 1
    counter_e = end - start - counter_a
    print(f" Số các số chia hết cho cả {print_divisors} là: {counter_a}")
    print(f" Số các số chia hết cho hoặc {nums[0]} hoặc {nums[1]} là: {counter_b}")
    print(
        f" Số các số chia hết cho {nums[0]} nhưng không cho {nums[2]} là: {counter_c}"
    )
    print(f" Số các số chia hết cho ít nhất một trong {print_divisors} là: {counter_d}")
    print(f" Số các số không chia hết cho cả {print_divisors} là: {counter_e}")
    print(
        f" Số các số chia hết cho {nums[1]} và {nums[2]} nhưng không cho {nums[0]} là: {counter_f}"
    )
    print(f" Số các số chia hết cho đúng 1 trong {print_divisors} là: {counter_g}")
    print(f" Số các số chia hết cho đúng 2 trong {print_divisors} là: {counter_h}")


count_divisor()
