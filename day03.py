def wires(filename='data/day03.txt'):
    with open(filename) as f:
        wire_1, wire_2 = f.read().strip().split('\n')
    return wire_1, wire_2


def calculate_path(wire):
    x, y, path = 0, 0, []
    for trace in wire.split(','):

        direction, move = trace[0], int(trace[1:])
        x_points, y_points = [x] * move, [y] * move

        if direction == 'R':
            x_points = range(x, x + move + 1)
            x += move
        elif direction == 'L':
            x_points = range(x, x - move - 1, -1)
            x -= move
        elif direction == 'U':
            y_points = range(y, y + move + 1)
            y += move
        elif direction == 'D':
            y_points = range(y, y - move - 1, -1)
            y -= move

        path.extend([(x_p, y_p) for x_p, y_p in zip(x_points, y_points)])
    return path


def intersections(wire_1, wire_2):
    path_1 = calculate_path(wire_1)
    path_2 = calculate_path(wire_2)
    return list(set(path_1[1:]) & set(path_2[1:]))


def manhattan(point):
    return abs(point[0]) + abs(point[1])


if __name__ == '__main__':

    wire_1, wire_2 = wires()

    points = intersections(wire_1, wire_2)
    dist = [manhattan(p) for p in points]
    print(min(dist))

    steps = [calculate_path(wire_1).index(p) + \
             calculate_path(wire_2).index(p) for p in points]
    print(min(steps))
