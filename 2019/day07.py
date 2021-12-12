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
        if opcode in [1, 2, 5, 6, 7, 8]:
            val_1 = ints[idx + 1] if not mode_C else idx + 1
            val_2 = ints[idx + 2] if not mode_B else idx + 2
            val_3 = ints[idx + 3]

            if opcode == 1:
                ints[val_3] = ints[val_1] + ints[val_2]
                idx += 4
            elif opcode == 2:
                ints[val_3] = ints[val_1] * ints[val_2]
                idx += 4
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
        elif opcode == 3:
            ints[ints[idx + 1]] = input_vals[0]
            idx += 2
            input_vals.pop(0)
        elif opcode == 4:
            val_1 = ints[idx + 1] if not mode_C else idx + 1
            diagnostic_code = ints[val_1]
            idx += 2
            return ints, diagnostic_code, idx


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
    print(max([thruster_signal(program, p) for p in permutations(range(5, 10))]))
