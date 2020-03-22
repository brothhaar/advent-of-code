import pathlib


class Orbit:

    def __init__(self, name, count, parent):
        self.name = name
        self.count = count
        self.parent = parent
        self.orbiters = []
        self.visited = False
        self.dist = 0
        print('Orbit', name)

    def add_orbiter(self, orbit):
        print('add_orbiter', self.name, orbit.name)
        self.orbiters.append(orbit)

    def set_parent(self, parent):
        self.parent = parent

    def __str__(self):
        return self.name

    def checksum(self, parent_count):
        self.count = parent_count + 1
        print('checksum', self.name, self.count, ', '.join(str(x) for x in self.orbiters))
        cs = self.count
        for orbit in self.orbiters:
            cs = cs + orbit.checksum(self.count)
        return cs

    def search(self, dist):
        self.visited = True
        print('searching %s, dist: %d' % (self.name, dist))
        for o in self.orbiters:
            if o.visited:
                continue
            elif o.name == 'SAN':
                print("FOUND %s at %d" % (o.name, dist))
                o.dist = dist
            else:
                o.search(dist + 1)
        if self.parent and not self.parent.visited:
            self.parent.search(dist + 1)


def build_orbits(orbits):
    orbit_map = {}
    for orbit in orbits:
        center_name = orbit.split(')')[0].rstrip()
        orbiter_name = orbit.split(')')[1].rstrip()
        if not orbit_map.get(center_name):
            orbit_map[center_name] = Orbit(center_name, 0, None)
        if not orbit_map.get(orbiter_name):
            orbit_map[orbiter_name] = Orbit(orbiter_name, 0, orbit_map[center_name])
        else:
            orbit_map[orbiter_name].set_parent(orbit_map[center_name])
        orbit_map.get(center_name).add_orbiter(orbit_map.get(orbiter_name))

    return orbit_map


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / 'input') as orbits:
        orbit_map = build_orbits(orbits)
        print('orbit_map', orbit_map)
        ans = orbit_map['COM'].checksum(-1)
        print('answer: %d' % ans)
