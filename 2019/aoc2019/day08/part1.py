import pathlib


class SpaceImageLayer:
    def __init__(self, img, length, width):
        self.img = list(img)
        self.length = length
        self.width = width
        self.data = []
        self.build()

    def build(self):
        size = self.length
        start = 0
        end = size
        for i in range(0, self.width):
            d = self.img[start:end]
            self.data.append(list(d))
            start = start + size
            end = end + size
        print(self)

    def do_filter(self, t):
        print("filtering on %s" % t, self.img)
        return len(list(filter(lambda d: d == t, self.img)))

    def __str__(self):
        return self.data.__str__()


class SpaceImage:
    def __init__(self, img, length, width):
        self.img = img
        self.layers = []
        self.length = length
        self.width = width
        self.build()

    def build(self):
        size = self.length * self.width
        layer_count = int(len(self.img) / size)
        print('layers', layer_count)
        start = 0
        end = size
        for i in range(0, layer_count):
            d = self.img[start:end]
            print(d)
            self.layers.append(SpaceImageLayer(d, self.length, self.width))
            start = start + size
            end = end + size

    def merge(self):
        merged = [["2" for i in range(0, self.length)] for i in range(0, self.width)]
        print("merged", merged)
        for layer in self.layers:
            for i in range(0, self.width):
                for j in range(0, self.length):
                    mi = merged[i][j]
                    if mi == "0" or mi == "1":
                        continue
                    else:
                        merged[i][j] = layer.data[i][j]
        final = [[" " for i in range(0, self.length)] for i in range(0, self.width)]
        for i in range(0, self.width):
            for j in range(0, self.length):
                if merged[i][j] == "1":
                    final[i][j] = "X"
        blah = []
        for i in range(0, self.width):
            blah.append(''.join(final[i]))
        print("merged", blah)
        return blah


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / 'input') as f:
        d = f.readline()
        si = SpaceImage(d, 25, 6)
        min_cnt = 999999999999
        layer = None
        for l in si.layers:
            cnt = l.do_filter("0")
            if cnt < min_cnt:
                min_cnt = cnt
                layer = l
        print("min 0s", layer)
        ones = layer.do_filter("1")
        print("ones", ones)
        twos = layer.do_filter("2")
        print("twos", twos)
        print("answer: %d" % (ones * twos))
