start = 206938
end = 679128


def get_digits(password):
    digits = []
    digits.append(int(password / 100000 % 10))
    digits.append(int(password / 10000 % 10))
    digits.append(int(password / 1000 % 10))
    digits.append(int(password / 100 % 10))
    digits.append(int(password / 10 % 10))
    digits.append(int(password / 1 % 10))
    print(digits)
    return digits


def check_part_2(digits):
    current = -1
    current_count = 0
    found_mult = False
    for digit in digits:
        if digit != current:
            if current_count == 2:
                return True
            current_count = 0
        current_count = current_count + 1
        print('digit %d current %d current_count %d' % (digit, current, current_count))
        current = digit
        if current_count > 2:
            found_mult = True
    return current_count == 2 or not found_mult


def check_password(password):
    digits = get_digits(password)
    #print("%d %d %d %d %d %d %d" % (password, d0, d1, d2, d3, d4, d5))
    return 99999 < password < 1000000 and (
        digits[0] == digits[1] or digits[1] == digits[2] or digits[2] == digits[3] or digits[3] == digits[4] or
        digits[4] == digits[5]) and (
               digits[0] <= digits[1] <= digits[2] <= digits[3] <= digits[4] <= digits[5]) and check_part_2(digits)


if __name__ == "__main__":
    count = 0
    for password in range(start, end + 1):
        if check_password(password):
            count = count + 1
    print('answer: %s' % count)
