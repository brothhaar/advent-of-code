from math import floor


def fuel(mass):
    return floor(mass / 3) - 2


with open('input') as masses:
    ans = 0
    for mass in masses:
        ans += fuel(int(mass))

print('answer: %d' % ans)
