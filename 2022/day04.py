"""
AOC: Day 4

Part 1:
- In how many assignment pairs does one range fully contain the other?

Part 2:
- In how many assignment pairs do the ranges overlap?
"""


def read_data(fn):

    with open(fn) as f:
        data = f.read().strip().split("\n")
    return data


def make_range(data):
    ranges = data.split(",")
    return [rng.split("-") for rng in ranges]


def contains(data):
    [x1, x2], [y1, y2] = make_range(data)

    if (int(x1) >= int(y1)) and (int(x2) <= int(y2)):
        return True
    if (int(y1) >= int(x1)) and (int(y2) <= int(x2)):
        return True
    return False


def overlaps(data):
    [x1, x2], [y1, y2] = make_range(data)

    if (int(x1) <= int(y2)) and (int(y1) <= int(x2)):
        return True
    if (int(y1) <= int(x2)) and (int(x1) <= int(y2)):
        return True
    return False


def num_contains(data):
    return sum(contains(d) for d in data)


def num_overlaps(data):
    return sum(overlaps(d) for d in data)


if __name__ == "__main__":

    data = read_data("data/day04.txt")

    print(f"Number of pairs fully containing the other: {num_contains(data)}")
    print(f"Number of pairs overlapping the other: {num_overlaps(data)}")
