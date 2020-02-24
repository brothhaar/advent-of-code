from aoc2019.day03.part1 import wires_intersect


def test_wires_intersect():
    assert wires_intersect('R1,U1',
                           'R1,U1') == 1
    assert wires_intersect('R1,U1',
                           'U1,R1') == 2
    assert wires_intersect('R8,U5,L5,D3',
                           'U7,R6,D4,L4') == 6
    assert wires_intersect('R75,D30,R83,U83,L12,D49,R71,U7,L72',
                           'U62,R66,U55,R34,D71,R55,D58,R83') == 159
    assert wires_intersect('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
                           'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7') == 135
