from aoc2019.day06.part1 import build_orbits


def test_checksum():
    orbit_map = build_orbits(
        ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN'])
    orbit_map['YOU'].search(-1)
    assert(orbit_map['SAN'].dist == 4)
