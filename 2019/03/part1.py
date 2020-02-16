import sys


def getKey(x, y):
    return '%d,%d' % (x, y)


class WireTrace:

    def __init__(self, wire_map):
        self.wire_map = wire_map

    def visit_point(self, x, y):
        pass

    def trace_right(self, x, y, dist):
        xend = x + dist
        for xp in range(x + 1, xend + 1):
            self.visit_point(xp, y)
        return xend, y

    def trace_left(self, x, y, dist):
        xend = x - dist
        for xp in range(x - 1, x - dist - 1, -1):
            self.visit_point(xp, y)
        return xend, y

    def trace_up(self, x, y, dist):
        yend = y + dist
        for yp in range(y + 1, y + dist + 1):
            self.visit_point(x, yp)
        return x, yend

    def trace_down(self, x, y, dist):
        yend = y - dist
        for yp in range(y - 1, y - dist - 1, -1):
            self.visit_point(x, yp)
        return x, yend

    def trace_segment(self, x, y, trace):
        print('trace_segment: %d, %d, %s' % (x, y, trace))
        direc = trace[0]
        dist = int(trace[1:])
        if direc == 'R':
            return self.trace_right(x, y, dist)
        elif direc == 'L':
            return self.trace_left(x, y, dist)
        elif direc == 'U':
            return self.trace_up(x, y, dist)
        elif direc == 'D':
            return self.trace_down(x, y, dist)

    def trace_wire(self, wire_str):
        segments = wire_str.split(',')
        x = 0
        y = 0
        for segment in segments:
            x, y = self.trace_segment(x, y, segment)


class WireTraceOne(WireTrace):

    def visit_point(self, x, y):
        key = getKey(x, y)
        # print('pt: %s' % key)
        self.wire_map[key] = 1


class WireTraceTwo(WireTrace):
    min_dist = sys.maxsize

    def visit_point(self, x, y):
        key = getKey(x, y)
        # print('pt: %s' % key)
        if key != '0,0' and key in self.wire_map:
            dist = abs(x) + abs(y)
            if dist < self.min_dist:
                self.min_dist = dist
            print('found intersection at %s, distance %d, min %d' % (key, dist, self.min_dist))


def wires_intersect(wire1_str, wire2_str):
    wire_map = {}
    wire1 = WireTraceOne(wire_map)
    wire1.trace_wire(wire1_str)
    wire2 = WireTraceTwo(wire_map)
    wire2.trace_wire(wire2_str)
    return wire2.min_dist


if __name__ == "__main__":
    with open('input') as f:
        wire1_str = f.readline()
        wire2_str = f.readline()
        ans = wires_intersect(wire1_str, wire2_str)
        print('answer: %s' % ans)
