"""
AOC: Day 1

Part 1:
- Find the Elf carrying the most Calories.
- How many total Calories is that Elf carrying?

Part 2:
- Find the top three Elves carrying the most Calories
- How many Calories are those Elves carrying in total?
"""


def read_data(fn):

    with open(fn) as f:
        data = f.read().strip().split("\n\n")
    return [d.split("\n") for d in data]


def sum_cals(cals):
    return [sum(map(int, cal)) for cal in cals]


def most_cals(total_cals):
    return total_cals.index(max(total_cals))


def top_cals(total_cals, n):
    return sorted(((val, ind) for ind, val in enumerate(total_cals)), reverse=True)[:n]


if __name__ == "__main__":

    cals = read_data("data/day01.txt")
    total_cals = sum_cals(cals)
    top1_elf = most_cals(total_cals)

    print(f"Elf is number {top1_elf}")
    print(f"With a total of {total_cals[top1_elf]}")

    top3_elf = top_cals(total_cals, 3)

    print(f"Top 3 elves are numbers {list(zip(*top3_elf))[1]}")
    print(f"With a total of {sum(list(zip(*top3_elf))[0])}")
