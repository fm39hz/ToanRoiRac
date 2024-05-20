def next_binary_string(bin_str):
    # Chuyển xâu nhị phân thành số nguyên
    num = int(bin_str, 2)
    # Thêm 1 vào số nguyên để được xâu nhị phân kế tiếp
    next_num = num + 1
    # Chuyển số nguyên trở lại xâu nhị phân
    next_bin_str = bin(next_num)[2:]  # Loại bỏ tiền tố '0b'
    # Đảm bảo xâu nhị phân có cùng độ dài với xâu ban đầu bằng cách thêm các số 0 ở đầu
    next_bin_str = next_bin_str.zfill(len(bin_str))
    return next_bin_str


def find_next_n_binary_strings(bin_str, n):
    result = []
    current_str = bin_str
    for _ in range(n):
        current_str = next_binary_string(current_str)
        result.append(current_str)
    return result


if __name__ == "__main__":
    bin_str = "1001100101"
    n = 10
    result = find_next_n_binary_strings(bin_str, n)
    print(f"10 xâu nhị phân liền sau của xâu nhị phân {bin_str}:")
    for bin_str in result:
        print(bin_str)
