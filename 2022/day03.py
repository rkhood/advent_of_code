"""
AOC: Day 3

Part 1:
- What is the sum of the priorities of those item types?

Part 2:
- What is the new sum of the priorities of those item types?
"""


def read_data(fn):

    with open(fn) as f:
        data = f.read().strip().split("\n")
    return data


def splitr(rucksack):

    comp1 = rucksack[:len(rucksack) // 2]
    comp2 = rucksack[len(rucksack) // 2:]
    return [comp1, comp2]


def duplicate(comps):
    return list(set.intersection(*map(set, comps)))[0]


def priority(dup):

    if dup.isupper():
        return ord(dup.lower()) - 70

    return ord(dup) - 96


def summed(rucksacks):
    """
    Part 1: 2 compartments in 1 rucksack
    """
    return sum(priority(duplicate(splitr(rucksack))) for rucksack in rucksacks)


def summed(rucksacks):
    """
    Part 2: 3 rucksacks
    """
    return sum(priority(duplicate(rucksack)) for rucksack in zip(*[iter(rucksacks)]*3))


if __name__ == "__main__":

    rucksacks = read_data("data/day03.txt")

    print(f"Sum of priorities is {summed(rucksacks)}")
