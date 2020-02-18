start = 206938
end = 679128


def check_password(password):
    d0 = int(password / 100000 % 10)
    d1 = int(password / 10000 % 10)
    d2 = int(password / 1000 % 10)
    d3 = int(password / 100 % 10)
    d4 = int(password / 10 % 10)
    d5 = int(password / 1 % 10)
    # print("%d %d %d %d %d %d %d" % (password, d0, d1, d2, d3, d4, d5))
    return 99999 < password < 1000000 and (d0 == d1 or d1 == d2 or d2 == d3 or d3 == d4 or d4 == d5) and (
            d0 <= d1 <= d2 <= d3 <= d4 <= d5)


if __name__ == "__main__":
    count = 0
    for password in range(start, end + 1):
        if check_password(password):
            count = count + 1
    print('answer: %s' % count)
