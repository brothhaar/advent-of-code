import sys
from part1 import WireTrace, getKey


class WireTraceDistance(WireTrace):
    distance = 0

    def visit_point(self, x, y):
        key = getKey(x, y)
        self.distance = self.distance + 1
        self.wire_map[key] = self.distance


def wires_intersect(wire1_str, wire2_str):
    wire1 = WireTraceDistance()
    wire1.trace_wire(wire1_str)
    wire2 = WireTraceDistance()
    wire2.trace_wire(wire2_str)

    intersects = set(wire1.wire_map.keys()) & set(wire2.wire_map.keys())
    min_dist = sys.maxsize
    for key in intersects:
        print('intersection: ', key)
        tot_dist = wire1.wire_map[key] + wire2.wire_map[key]
        if tot_dist < min_dist:
            min_dist = tot_dist

    return min_dist


if __name__ == "__main__":
    with open('input') as f:
        wire1_str = f.readline()
        wire2_str = f.readline()
        ans = wires_intersect(wire1_str, wire2_str)
        print('answer: %s' % ans)
