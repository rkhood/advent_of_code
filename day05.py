def read_data(filename='data/day05.txt'):
    with open(filename) as f:
        program = [int(i) for i in f.read().split(',')]
    return program


def intcode(program, input_val=1):
    program[1] = 12
    program[2] = 2
    ints = program.copy()
    idx = 0
    while ints[idx] != 99:

        if len(str(opcode)) > 1:
            new_opcode = int(str(opcode)[-2:])
            params = [int(i) for i in str(opcode)[:-2]][::-1]
            mode_A, mode_B, mode_C = [0] * (3 - len(params)) + params

        opcode = ints[idx]
        val_1 = ints[idx + 1] if mode_C else idx + 1
        val_2 = ints[idx + 2] if mode_B else idx + 2
        val_3 = ints[idx + 3] if mode_A else idx + 3

        if opcode == 1:
            ints[val_3] = ints[val_1] + ints[val_2]
            idx += 4
        elif opcode == 2:
            ints[val_3] = ints[val_1] * ints[val_2]
            idx += 4
        elif opcode == 3:
            ints[val_3] = input_val
            idx += 2
        elif opcode == 4:
            print(val_1)
            idx += 2


    return ints#[0]


if __name__ == '__main__':

    program = read_data()
    print(intcode(program))
