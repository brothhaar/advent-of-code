from math import floor


def fuel(mass):
    f = floor(mass / 3) - 2
    if f <= 0:
        return 0
    return f + fuel(f)


if __name__ == "__main__":
    with open('input') as masses:
        ans = 0
        for mass in masses:
            ans += fuel(int(mass))

    print('answer: %d' % ans)
