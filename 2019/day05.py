def read_data(filename='data/day05.txt'):
    with open(filename) as f:
        program = [int(i) for i in f.read().split(',')]
    return program


def intcode(program, input_val=1):
    ints = program.copy()

    diagnostic_code, idx = 0, 0
    while ints[idx] != 99:
        opcode = ints[idx]

        mode_A, mode_B, mode_C = 0, 0, 0
        if opcode > 100:
            str_op = str(opcode)
            opcode = int(str_op[-2:])
            params = [int(i) for i in str_op[:-2]]
            mode_A, mode_B, mode_C = [0] * (3 - len(params)) + params

        val_1 = ints[idx + 1] if not mode_C else idx + 1
        val_2 = ints[idx + 2] if not mode_B else idx + 2
        val_3 = ints[idx + 3]

        if opcode == 1:
            ints[val_3] = ints[val_1] + ints[val_2]
            idx += 4
        elif opcode == 2:
            ints[val_3] = ints[val_1] * ints[val_2]
            idx += 4
        elif opcode == 3:
            ints[val_1] = input_val
            idx += 2
        elif opcode == 4:
            diagnostic_code = ints[val_1]
            idx += 2
        elif opcode == 5:
            if ints[val_1] != 0:
                idx = ints[val_2]
            else:
                idx += 3
        elif opcode == 6:
            if ints[val_1] == 0:
                idx = ints[val_2]
            else:
                idx += 3
        elif opcode == 7:
            if ints[val_1] < ints[val_2]:
                ints[val_3] = 1
            else:
                ints[val_3] = 0
            idx += 4
        elif opcode == 8:
            if ints[val_1] == ints[val_2]:
                ints[val_3] = 1
            else:
                ints[val_3] = 0
            idx += 4

    return diagnostic_code


if __name__ == '__main__':

    program = read_data()
    print(intcode(program, input_val=1))
    print(intcode(program, input_val=5))
