from itertools import permutations


def read_data(filename='data/day07.txt'):
    with open(filename) as f:
        program = [int(i) for i in f.read().split(',')]
    return program


def intcode(program, input_vals):
    ints = program.copy()

    diagnostic_code, idx, input_counter = 0, 0, 0
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
            ints[val_1] = input_vals[input_counter]
            idx += 2
            if len(input_vals) > 1:
                input_counter += 1
            if input_counter > 1:
                input_counter -= 1
        elif opcode == 4:
            diagnostic_code = ints[val_1]
            idx += 2
            return diagnostic_code
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


def thruster_signal(program, phases):
    diag_code = 0
    for phase in phases:
        diag_code = intcode(program, input_vals=[phase, diag_code])
    return diag_code


def thruster_signal_feedback(program, phases):
    diag_code = thruster_signal(program, phases)
    while True:
        diag_code_start = diag_code
        diag_code = intcode(program, input_vals=[diag_code])
        if diag_code < diag_code_start:
            break
    return diag_code


if __name__ == '__main__':

#    program = read_data()
#    print(max([thruster_signal(program, phase
#        ) for phase in permutations(range(5))]))


#    range(5, 10)

    phase_seq = [9,8,7,6,5]
    program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    print(thruster_signal_feedback(program, phase_seq))
