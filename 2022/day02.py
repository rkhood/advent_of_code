"""
AOC: Day 2

Part 1:
- What would your total score be if everything goes exactly according to your
  strategy guide?

Part 2:
- What would your total score be if everything goes exactly according to your
  new strategy guide?
"""


def read_data(fn):

    with open(fn) as f:
        data = f.read().strip().split("\n")
    return data


def translate(play):

    map_play = {
        "A": "X",
        "B": "Y",
        "C": "Z",
    }
    return map_play[play]


def shape(play):

    map_shape = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    return map_shape[play]


def result(elf, me):

    if me == elf:
        return 3

    if (
        (me == "X" and elf == "Z") or
        (me == "Y" and elf == "X") or
        (me == "Z" and elf == "Y")
    ):
        return 6

    return 0


def score(game):
    """
    Part 1: XYZ is play
    """
    elf, me = game.split()
    elf = translate(elf)
    return result(elf, me) + shape(me)


def score(game):
    """
    Part 2: XYZ is outcome
    """
    elf, me = game.split()
    elf = translate(elf)

    if me == "Y":
        return 3 + shape(elf)

    if me == "Z":
        return [6 + shape(play) for play in "XYZ" if result(elf, play) == 6][0]

    return [shape(play) for play in "XYZ" if result(elf, play) == 0][0]


def total_score(games):
    return sum(score(game) for game in games)


if __name__ == "__main__":

    games = read_data("data/day02.txt")

    print(f"Total score is {total_score(games)}")
