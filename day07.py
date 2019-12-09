from itertools import permutations


def read_data(filename='data/day07.txt'):
    with open(filename) as f:
        program = [int(i) for i in f.read().split(',')]
    return program


def intcode(program, input_vals, idx=0):
    ints = program.copy()
    while True:
        opcode = ints[idx]

        mode_A, mode_B, mode_C = 0, 0, 0
        if opcode > 100:
            str_op = str(opcode)
            opcode = int(str_op[-2:])
            params = [int(i) for i in str_op[:-2]]
            mode_A, mode_B, mode_C = [0] * (3 - len(params)) + params
        print(idx)
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
            ints[val_1] = input_vals[0]
            idx += 2
            input_vals.pop(0)
        elif opcode == 4:
            diagnostic_code = ints[val_1]
            idx += 2
            return ints, diagnostic_code, idx
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
        elif opcode == 99:
            return ints, None, idx


def thruster_signal(program, phases):
    signal = 0

    index = [0] * len(phases)
    diag_codes = [0] * len(phases)
    inputs = [[phases[phase]] for phase in range(len(phases))]
    inputs[0].append(0)
    programs = [program[:]] * len(phases)

    done = False
    while not done:
        for i in range(len(phases)):
            programs[i], new_diag_code, new_index = intcode(programs[i], inputs[i], index[i])
            if new_diag_code is None:
                if diag_codes[-1] > signal:
                    signal = diag_codes[-1]
                done = True
                break
            index[i] = new_index
            diag_codes[i] = new_diag_code
            inputs[(i + 1) % len(inputs)].append(new_diag_code)
    return signal


if __name__ == '__main__':

    program = read_data()

    print(max([thruster_signal(program, p) for p in permutations(range(5))]))

#    phase_seq = [9,8,7,6,5]
#    program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
#    program = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
#    print(thruster_signal(program, phase_seq))
    print(max([thruster_signal(program, p) for p in permutations(range(5, 10))]))
