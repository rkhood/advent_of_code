def read_data(filename='data/day02.txt'):
    with open(filename) as f:
        program = [int(i) for i in f.read().strip().split(',')]
    return program


def intcode(ints):
    idx = 0
    while idx < len(ints):
        if ints[idx] == 1:
            ints[ints[idx + 3]] = ints[ints[idx + 1]] + ints[ints[idx + 2]]
        elif ints[idx] == 2:
            ints[ints[idx + 3]] = ints[ints[idx + 1]] * ints[ints[idx + 2]]
        idx += 4
    return ints[0]


def restore_gravity(ints, noun=12, verb=2):
    ints[1] = noun
    ints[2] = verb
    return ints


def find_noun_verb(ints):
    for noun in range(100):
        for verb in range(100):
            if intcode(restore_gravity(ints[:], noun, verb)) == 19690720:
                return 100 * noun + verb


if __name__ == '__main__':

    program = read_data()
    print(intcode(restore_gravity(program[:])))
    print(find_noun_verb(program))
