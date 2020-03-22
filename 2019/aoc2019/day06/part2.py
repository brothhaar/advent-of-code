import pathlib
from aoc2019.day06.part1 import build_orbits, Orbit


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / 'input') as orbits:
        orbit_map = build_orbits(orbits)
        ans = orbit_map['YOU'].search(-1)
        print('answer: %d' % orbit_map['SAN'].dist)