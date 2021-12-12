def read_data(filename='data/day02.txt'):
    with open(filename) as f:
        program = [int(i) for i in f.read().strip().split(',')]
    return program


def intcode(program):
    ints = program.copy()
    idx = 0
    while ints[idx] != 99:
        opcode, param1, param2, output = ints[idx:idx + 4]
        if opcode == 1:
            ints[output] = ints[param1] + ints[param2]
        elif opcode == 2:
            ints[output] = ints[param1] * ints[param2]
        idx += 4
    return ints[0]


def restore_gravity(program, noun=12, verb=2):
    program[1] = noun
    program[2] = verb
    return program


def find_noun_verb(program):
    for noun in range(100):
        for verb in range(100):
            if intcode(restore_gravity(program, noun, verb)) == 19690720:
                return 100 * noun + verb


if __name__ == '__main__':

    program = read_data()
    print(intcode(restore_gravity(program)))
    print(find_noun_verb(program))
