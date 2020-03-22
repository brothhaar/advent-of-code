from aoc2019.day08.part1 import SpaceImage, SpaceImageLayer
import pathlib


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / 'input') as f:
        d = f.readline()
        si = SpaceImage(d, 25, 6)
        merged = si.merge()
        print("answer:")
        for l in merged:
            print(l)
