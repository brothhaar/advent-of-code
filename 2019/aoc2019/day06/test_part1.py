from aoc2019.day06.part1 import build_orbits


def test_checksum():
    orbit_map = build_orbits(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L'])
    assert orbit_map['COM'].checksum(-1) == 42
